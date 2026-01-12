"""
4" Schedule 80 Pipe with Weld Prep Bevels
Standard ASME/API weld prep: 37.5° bevel with 1/16" (0.0625") land
"""

import cadquery as cq
import math

# ============================================
# PIPE PARAMETERS - 4" Schedule 80
# ============================================
NPS = 4.0                    # Nominal Pipe Size
OD = 4.500                   # Outside Diameter (inches)
WALL = 0.337                 # Wall Thickness (inches) - Sch 80
ID = OD - (2 * WALL)         # Inside Diameter = 3.826"
LENGTH = 12.0                # Overall length (inches)

# ============================================
# WELD PREP PARAMETERS
# ============================================
BEVEL_ANGLE = 37.5           # Standard ASME/API bevel angle (degrees)
LAND = 0.0625                # 1/16" land (inches)

# Calculate bevel depth (how far the bevel cuts into the wall)
# The bevel goes from OD down to (ID + 2*LAND)
BEVEL_DEPTH = WALL - LAND    # = 0.337 - 0.0625 = 0.2745"

# Calculate bevel height (axial distance the bevel takes)
# tan(37.5°) = bevel_depth / bevel_height
# bevel_height = bevel_depth / tan(37.5°)
BEVEL_HEIGHT = BEVEL_DEPTH / math.tan(math.radians(BEVEL_ANGLE))

print("=" * 50)
print("4\" Schedule 80 Pipe - Weld Prep Details")
print("=" * 50)
print(f"Outside Diameter (OD):  {OD:.3f}\"")
print(f"Wall Thickness:         {WALL:.3f}\"")
print(f"Inside Diameter (ID):   {ID:.3f}\"")
print(f"Pipe Length:            {LENGTH:.3f}\"")
print("-" * 50)
print(f"Bevel Angle:            {BEVEL_ANGLE}°")
print(f"Land:                   {LAND:.4f}\" (1/16\")")
print(f"Bevel Depth:            {BEVEL_DEPTH:.4f}\"")
print(f"Bevel Height:           {BEVEL_HEIGHT:.4f}\"")
print("=" * 50)

# ============================================
# CREATE THE PIPE BODY
# ============================================

# Start with a solid cylinder (OD)
pipe = (
    cq.Workplane("XY")
    .circle(OD / 2)           # Outer radius
    .extrude(LENGTH)          # Extrude full length
)

# Hollow it out (create the bore)
pipe = (
    pipe
    .faces(">Z")              # Select top face
    .workplane()
    .circle(ID / 2)           # Inner radius
    .cutThruAll()             # Cut through entire length
)

# ============================================
# CREATE BEVEL AT TOP END (Z = LENGTH)
# ============================================
# The bevel profile is a ring that we revolve
# Starting at OD, angling down to the land

# Create a 2D profile for the bevel cut (triangular ring cross-section)
# We'll create this on XZ plane and revolve around Z axis

bevel_top = (
    cq.Workplane("XZ")
    .moveTo(OD/2, LENGTH)                          # Start at OD, top
    .lineTo(OD/2, LENGTH - BEVEL_HEIGHT)           # Go down on OD
    .lineTo(ID/2 + LAND, LENGTH)                   # Angle to land
    .close()                                        # Close the triangle
    .revolve(360, (0, LENGTH), (0, 1))             # Revolve around Z axis at top
)

# Cut the bevel from the pipe
pipe = pipe.cut(bevel_top)

# ============================================
# CREATE BEVEL AT BOTTOM END (Z = 0)
# ============================================
bevel_bottom = (
    cq.Workplane("XZ")
    .moveTo(OD/2, 0)                               # Start at OD, bottom
    .lineTo(OD/2, BEVEL_HEIGHT)                    # Go up on OD
    .lineTo(ID/2 + LAND, 0)                        # Angle to land
    .close()                                        # Close the triangle
    .revolve(360, (0, 0), (0, 1))                  # Revolve around Z axis at bottom
)

# Cut the bevel from the pipe
pipe = pipe.cut(bevel_bottom)

# ============================================
# EXPORT TO STEP FILE
# ============================================
output_file = "Pipe4-SCH80-12in-BEVELED.step"
cq.exporters.export(pipe, output_file)
print(f"\n✓ Exported: {output_file}")

# Also export STL for quick viewing if needed
stl_file = "Pipe4-SCH80-12in-BEVELED.stl"
cq.exporters.export(pipe, stl_file)
print(f"✓ Exported: {stl_file}")

print("\nDone! Open the STEP file in your CAD viewer.")
