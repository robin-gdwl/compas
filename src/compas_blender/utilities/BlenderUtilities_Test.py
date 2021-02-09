"""
Test-script to be run inside Blender that checks all utility functions

"""
import compas_blender

# Clear scene and Data
compas_blender.clear()

# Collections
print("Collection Utilities: ")

testcol = compas_blender.create_collection("testcollection")
print(testcol)

testcols = compas_blender.create_collections(["C_one", "C_two", "C_three"])
nested_testcols = compas_blender.create_collections_from_path("TOPLEVEL-COLLECTION::NESTED-COLLECTION1::NESTED-COLLECTION2")

compas_blender.clear_collection("C_two")
compas_blender.clear_collections(["C_one", "C_three"])

# Data
compas_blender.delete_unused_data()

# Document

print("Basename :  ", compas_blender.get_document_basename())
print("Filename :  ", compas_blender.get_document_filename())
print("Extension:  ", compas_blender.get_document_extension())
print("Filepath :  ", compas_blender.get_document_filepath())
print("Directory:  ", compas_blender.get_document_dirname())

# Drawing

# Objects

# compas_blender.clear()
