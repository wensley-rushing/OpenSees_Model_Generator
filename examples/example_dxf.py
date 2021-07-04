import time
import modeler
import solver
import numpy as np

# Define a building
b = modeler.Building()

# Add levels - single-story building
b.add_level("base", 0.00, "fixed")
# b.add_level('1', 120.00)

for i in range(1, 7):
    b.add_level(str(i), 120*i)


# add girdlines
b.add_gridlines_from_dxf("examples/dxf/gridlines.dxf")


# Add goups
b.add_group('cols')
b.add_group('bms')
b.add_group('braces')

# define materials
b.materials.enable_Steel02()
b.set_active_material('steel')

# define sections
b.add_sections_from_json(
    "section_data/sections.json",
    "W",
    ["W14X90"])

b.add_sections_from_json(
    "section_data/sections.json",
    "HSS",
    ["HSS22X22X3/4", "HSS18X18X3/4", "HSS14X14X3/4",
     "HSS9X9X5/16"])

b.set_active_levels("all_above_base")
b.assign_surface_DL(1.00)
b.set_active_levels(["6"])
b.assign_surface_DL(1.20)

modeling_type = {'type': 'fiber', 'n_x': 5, 'n_y': 5}
# modeling_type = {'type': 'elastic'}

# define columns
b.set_active_groups(['cols'])
b.set_active_levels([str(i) for i in range(1, 2)])
b.set_active_section("HSS22X22X3/4")
b.add_columns_from_grids(
    n_sub=1,
    model_as=modeling_type)
b.set_active_levels([str(i) for i in range(2, 5)])
b.set_active_section("HSS18X18X3/4")
b.add_columns_from_grids(
    n_sub=1,
    model_as=modeling_type)
b.set_active_levels([str(i) for i in range(5, 7)])
b.set_active_section("HSS14X14X3/4")
b.add_columns_from_grids(
    n_sub=1,
    model_as=modeling_type)

# define beams
b.set_active_groups(['bms'])
b.set_active_levels("all_above_base")
b.set_active_section("W14X90")
b.set_active_placement('top_center')
b.add_beams_from_grids(n_sub=1, model_as=modeling_type,
                       ends={'type': 'RBS',
                             'dist': 0.05,
                             'length': 5,
                             'factor': 0.50})

# define brace elements
b.clear_gridlines()
b.add_gridlines_from_dxf("examples/dxf/gridlines_brace.dxf")
b.set_active_section("HSS9X9X5/16")
b.set_active_groups(['braces'])
b.add_braces_from_grids(btype="single", n_sub=12, camber=0.01,
                        model_as=modeling_type, release_distance=0.005)

b.preprocess()

b.plot_building_geometry(extrude_frames=False, frame_axes=False)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  nonlinear pushover analysis  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# # performing a nonlinear pushover analysis
# pushover_analysis = solver.PushoverAnalysis(b)
# control_node = b.list_of_parent_nodes()[-1]  # top floor
# # control_node = b.list_of_nodes()[-1]  # top floor somewhere

# t0 = time.time()
# analysis_metadata = pushover_analysis.run(
#     "y",
#     80.,
#     control_node,
#     1.,
#     np.linspace(0., 80., 80))
# n_plot_steps = analysis_metadata['successful steps']
# t1 = time.time()

# print(t1-t0)

# # plot the deformed shape for any of the steps
# plot_metadata = pushover_analysis.deformed_shape(
#     step=n_plot_steps-1, scaling=0.00, extrude_frames=False)
# print(plot_metadata)

# # plot pushover curve
# pushover_analysis.plot_pushover_curve("y", control_node)
# pushover_analysis.basic_forces(step=n_plot_steps-1)
