import matplotlib.pyplot as plt

CONSTELLATION_A = [
  (71, 73),
  (99, 47),
  (128, 54),
  (136, 80),
  (112, 105),
  (111, 141),
  (146, 153),
  (180, 145),
  (170, 104)
]

CONSTELLATION_B = [
  (130, 285),
  (159, 309),
  (193, 315),
  (233, 318),
  (269, 326),
  (289, 323),
  (273, 305),
  (245, 299),
  (241, 275),
  (243, 226),
  (214, 244),
  (284, 276),
  (302, 252)
]

x_coords_a, y_coords_a = zip(*CONSTELLATION_A)
x_coords_b, y_coords_b = zip(*CONSTELLATION_B)

plt.figure(figsize=(8, 6))
plt.scatter(x_coords_a, y_coords_a, color='red', label='Constellation A')
plt.scatter(x_coords_b, y_coords_b, color='blue', label='Constellation B')

plt.title("Star Constellations")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)
plt.legend()

plt.gca().set_xlim(0, 375)
plt.gca().set_ylim(0, 375)

plt.savefig("star_constellations.png")