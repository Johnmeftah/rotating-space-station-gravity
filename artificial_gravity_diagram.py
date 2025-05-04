
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# inertial frame 
ax1 = axes[0]
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)
ax1.set_aspect('equal')
ax1.set_title("Inertial Frame")

# outer ring
circle1 = patches.Circle((0, 0), 2, fill=False)
ax1.add_patch(circle1)

# inner circle (hole in donut)
circle2 = patches.Circle((0, 0), 0.8, fill=False)
ax1.add_patch(circle2)

# angular velocity label
ax1.annotate(r'$\\Omega$', xy=(-1.8, 1.5), fontsize=16)

# astronaut (square) on outer edge
ax1.plot(2, 0, 's', color='black', markersize=12)

# acceleration vector A (inward)
ax1.arrow(2, 0, -0.6, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
ax1.text(1.4, 0.1, r'$A$', fontsize=14)

# normal force vector N (inward)
ax1.arrow(2, 0, -0.4, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax1.text(1.6, -0.2, r'$N$', fontsize=14)

ax1.text(0, -2.3, "inertial\nframe", ha='center', fontsize=12)
ax1.axis('off')

# astronaut frame
ax2 = axes[1]
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-2.5, 2.5)
ax2.set_aspect('equal')
ax2.set_title("Astronaut's Frame")

# outer ring
circle3 = patches.Circle((0, 0), 2, fill=False)
ax2.add_patch(circle3)

# inner circle (hole in donut)
circle4 = patches.Circle((0, 0), 0.8, fill=False)
ax2.add_patch(circle4)

# astronaut (square)
ax2.plot(2, 0, 's', color='black', markersize=12)

# normal force vector N (inward)
ax2.arrow(2, 0, -0.4, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax2.text(1.6, 0.1, r'$N$', fontsize=14)

# fictitious force vector -mA (outward)
ax2.arrow(2, 0, 0.6, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
ax2.text(2.4, -0.2, r'$-mA$', fontsize=14)

ax2.text(2, 0.5, "at rest", fontsize=12)
ax2.text(0, -2.3, "astronaut's\nframe", ha='center', fontsize=12)
ax2.axis('off')

plt.tight_layout()
plt.show()
