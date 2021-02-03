# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26

@author: Dan

To adjust for .pdf oddities, create pandas dataframes via hardcoding the data.
Place frames in an array and return the array.
"""


import pandas as pd

# create the dataframes
# MCD12Q1 Science Data Sets
d = {
'SDS_Full_Name': ['Land Cover Type 1', 'Land Cover Type 2',
                  'Land Cover Type 3', 'Land Cover Type 4',
                  'Land Cover Type 5', 'Land Cover Property 1',
                  'Land Cover Property 2', 'Land Cover Property 3', 
                  'Land Cover Property 1 Assessment',
                  'Land Cover Property 2 Assessment',
                  'Land Cover Property 3 Assessment', 'Land Cover QC',
                  'Land Water Mask'],
'Short_Name': ['LC_Type1', 'LC_Type2', 'LC_Type3', 'LC_Type4', 'LC_Type5',
               'LC_Prop1', 'LC_Prop2', 'LC_Prop3', 'LC_Prop1_Assessment',
               'LC_Prop2_Assessment', 'LC_Prop3_Assessment', 'QC', 'LW'],
'Description': ['Annual IGBP classification', 'Annual UMD classification',
                'Annual LAI classification', 'Annual BGC classification',
                'Annual PFT classification', 'LCCS1 land cover layer',
                'LCCS2 land use layer', 'LCCS3 surface hydrology layer',
                'LCCS1 land cover layer confidence',
                'LCCS2 land use layer confidence',
                'LCCS3 surface hydrology layer confidence',
                'Product quality flags',
                'Binary land (class 2) / water (class 1) mask derived from MOD44W'],
'Units': ['Class #', 'Class #', 'Class #', 'Class #',
          'Class #', 'Class #', 'Class #', 'Class #',
          'Percent x 100', 'Percent x 100', 'Percent x 100',
          'Flags', 'Class #'],
'Data_Type': ['8-bit unsigned', '8-bit unsigned', '8-bit unsigned',
              '8-bit unsigned', '8-bit unsigned', '8-bit unsigned',
              '8-bit unsigned', '8-bit unsigned', '8-bit unsigned',
              '8-bit unsigned', '8-bit unsigned', '8-bit unsigned',
              '8-bit unsigned'],
'Valid_Range': ['[1,17]', '[0,15]', '[0,10]', '[0,8]', '[0,11]', '[1,43]', '[1,40]',
          '[1,51]', '[0,100]', '[0,100]', '[0,100]', '[0,10]', '[1,2]'], 
'Fill_Value': ['255', '255', '255', '255', '255', '255', '255', '255', '255',
          '255', '255', '255', '255']}
table1 = pd.DataFrame(data=d)

# MCD12C1 Science Data Sets
d = {
'Full_SDS_name': ['Majority Land Cover Type 1',
                  'Majority Land Cover Type 1 Assessment', 
                  'Majority Land Cover Type 1 Percent',
                  'Majority Land Cover Type 2',
                  'Majority Land Cover Type 2 Assessment', 
                  'Majority Land Cover Type 2 Percent',
                  'Majority Land Cover Type 3',
                  'Majority Land Cover Type 3 Assessment', 
                  'Majority Land Cover Type 3 Percent'],
'Short_Name': ['MLCT_1', 'MLCT_1_A', 'LCT_1_P',
               'MLCT_2', 'MLCT_2_A', 'LCT_2_P',
               'MLCT_3', 'MLCT_3_A', 'LCT_3_P'],
'Description': ['Most likely IGBP class for each 0.05 degree pixel',
                'Majority IGBP class confidence',
                'Percent cover of each IGBP class at each pixel',
                'Most likely UMD class for each 0.05 degree pixel',
                'Majority UMD class confidence (filled withland/water mask)',
                'Percent cover of each UMD class at each pixel',
                'Most likely LAI class for each 0.05 degree pixel',
                'Majority LAI class confidence (filled withland/water mask)',
                'Percent cover of each LAI class at each pixel'],
'Unit': ['Class value', 'Percent x 100', 'Percent x 100',
         'Class value', 'Percent x 100', 'Percent x 100',
         'Class value', 'Percent x 100', 'Percent x 100'],
'Data_Type': ['8-bit unsigned integer', '8-bit unsigned integer',
              '8-bit unsigned integer', '8-bit unsigned integer',
              '8-bit unsigned integer', '8-bit unsigned integer',
              '8-bit unsigned integer', '8-bit unsigned integer',
              '8-bit unsigned integer'],
'Valid_range': ['[0,16]', '[0,100]', '[0,100]', '[0,15]', '[0,100]', '[0,100]',
                '[0,10]', '[0,100]', '[0,100]'], 
'Fill_Value': ['255', '255', '255', '255', '255', '255', '255', '255', '255']}
table2 = pd.DataFrame(data=d)

# MCD12Q1 International Geosphere-Biosphere Programme (IGBP) legend and class 
# descriptions
d = {
'Name': ['Evergreen Needleleaf Forests', 'Evergreen Broadleaf Forests',
          'Deciduous Needleleaf Forests','Deciduous Broadleaf Forests',
          'Mixed Forests', 'Closed Shrublands', 'Open Shrublands',
          'Woody Savannas', 'Savannas', 'Grasslands', 'Permanent Wetlands',
          'Croplands', 'Urban and Built-up Lands',
          'Cropland/Natural Vegetation Mosaics', 'Permanent Snow and Ice',
          'Barren', 'Water Bodies', 'Unclassified'],
'Value': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
          '14', '15', '16', '17', '255'],
'Description': ['Dominated by evergreen conifer trees (canopy>2m). ' +
                'Tree cover >60%.',
                'Dominated by evergreen broadleaf and ' +
                'palmatetrees (canopy >2m). Tree cover >60%.',
                'Dominated by deciduous needleleaf (larch) trees ' +
                '(canopy >2m). Tree cover >60%.',
                'Dominated by deciduous broadleaf trees (canopy>2m). ' +
                'Tree cover >60%.',
                'Dominated by neither deciduous nor evergreen (40-60% ' +
                'of each) tree type (canopy >2m). Treecover >60%.',
                'Dominated by woody perennials (1-2m height) >60% cover.',
                'Dominated by woody perennials (1-2m height) 10-60% cover.',
                'Tree cover 30-60% (canopy >2m).',
                'Tree cover 10-30% (canopy >2m).',
                'Dominated by herbaceous annuals (<2m).',
                'Permanently inundated lands with 30-60% water cover and ' +
                '>10% vegetated cover.',
                'At least 60% of area is cultivated cropland.',
                'At least 30% impervious surface area including building ' +
                'materials, asphalt, and vehicles.',
                'Mosaics of small-scale cultivation 40-60% with natural ' +
                'tree, shrub, or herbaceous vegetation.',
                'At least 60% of area is covered by snow and ice for at ' +
                'least 10 months of the year.',
                'At least 60% of area is non-vegetated barren (sand, rock, ' +
                'soil) areas with less than 10% vegetation.',
                'At least 60% of area is covered by permanent water bodies.',
                'Has not received a map label because of missing inputs.']}
table3 = pd.DataFrame(data=d)

# University of Maryland (UMD) legend and class definitions.
d = {
'Name': ['Water Bodies',
         'Evergreen Needleleaf Forests', 'Evergreen Broadleaf Forests',
         'Deciduous Needleleaf Forests','Deciduous Broadleaf Forests',
         'Mixed Forests', 'Closed Shrublands', 'Open Shrublands',
         'Woody Savannas', 'Savannas', 'Grasslands', 'Permanent Wetlands',
         'Croplands', 'Urban and Built-up Lands',
         'Cropland/Natural Vegetation Mosaics', 'Non-Vegetated Lands',
         'Unclassified'],
'Value': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
          '13', '14', '15', '255'],
'Description': ['At least 60% of area is covered by permanent water bodies.',
                'Dominated by evergreen conifer trees (canopy>2m). ' +
                'Tree cover >60%.',
                'Dominated by evergreen broadleaf and ' +
                'palmatetrees (canopy >2m). Tree cover >60%.',
                'Dominated by deciduous needleleaf (larch) trees ' +
                '(canopy >2m). Tree cover >60%.',
                'Dominated by deciduous broadleaf trees (canopy>2m). ' +
                'Tree cover >60%.',
                'Dominated by neither deciduous nor evergreen (40-60% ' +
                'of each) tree type (canopy >2m). Treecover >60%.',
                'Dominated by woody perennials (1-2m height) >60% cover.',
                'Dominated by woody perennials (1-2m height) 10-60% cover.',
                'Tree cover 30-60% (canopy >2m).',
                'Tree cover 10-30% (canopy >2m).',
                'Dominated by herbaceous annuals (<2m).',
                'Permanently inundated lands with 30-60% water cover and ' +
                '>10% vegetated cover.',
                'At least 60% of area is cultivated cropland.',
                'At least 30% impervious surface area including building ' +
                'materials, asphalt, and vehicles.',
                'Mosaics of small-scale cultivation 40-60% with natural ' +
                'tree, shrub, or herbaceous vegetation.',
                'At least 60% of area is non-vegetated barren (sand, rock, ' +
                'soil) or permanent snow and ice with less than 10% ' +
                'vegetation.',
                'Has not received a map label because of missing inputs.']}
table4 = pd.DataFrame(data=d)

# Leaf Area Index (LAI) legend and class definitions.
d = {
'Name': ['Water Bodies', 'Grasslands', 'Shrublands', 'Broadleaf Croplands',
         'Savannas', 'Evergreen Broadleaf Forests',
         'Deciduous Broadleaf Forests', 'Evergreen Needleleaf Forests',
         'Deciduous Needleleaf Forests', 'Non-Vegetated Lands',
         'Urban and Built-up Lands', 'Unclassified'],
'Value': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '255'],
'Description': ['At least 60% of area is covered by permanent water bodies.',
                'Dominated by herbaceous annuals (<2m) including cereal ' +
                'croplands.',
                'Shrub (1-2m) cover >10%.',
                'Dominated by herbaceous annuals (<2m) that are cultivated ' +
                'with broadleaf crops.',
                'Between 10-60% tree cover (>2m).',
                'Dominated by evergreen broadleaf and palmate trees (>2m). ' +
                'Tree cover >60%.',
                'Dominated by deciduous broadleaf trees (>2m). Tree cover ' +
                '>60%.',
                'Dominated by evergreen conifer trees (>2m). Tree cover >60%.',
                'Dominated by deciduous needleleaf (larch) trees (>2m). ' +
                'Tree cover >60%.',
                'At least 60% of area is non-vegetated barren (sand, rock, ' +
                'soil) or permanent snow and ice with less than 10% ' +
                'vegetation.',
                'At least 30% impervious surface area including building ' +
                'materials, asphalt, and vehicles.',
                'Has not received a map label because of missing inputs.']}
table5 = pd.DataFrame(data=d)


# BIOME-Biogeochemical Cycles (BGC) legend and class definitions.
d = {
'Name': ['Water Bodies', 'Evergreen Needleleaf Vegetation',
         'Evergreen Broadleaf Vegetation', 'Deciduous Needleleaf Vegetation',
         'Deciduous Broadleaf Vegetation', 'Annual Broadleaf Vegetation',
         'Annual Grass Vegetation', 'Non-Vegetated Lands',
         'Urban and Built-up Lands', 'Unclassified'],
'Value': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '255'],
'Description': ['At least 60% of area is covered by permanent water bodies.',
                'Dominated by evergreen conifer trees and shrubs (>1m). ' +
                'Woody vegetation cover >10%.',
                'Dominated by evergreen broadleaf and palmate trees and ' +
                'shrubs (>1m). Woody vegetation cover >10%.',
                'Dominated by deciduous needleleaf (larch) trees and shrubs ' +
                '(>1m). Woody vegetation cover >10%.',
                'Dominated by deciduous broadleaf trees and shrubs (>1m). ' +
                'Woody vegetation cover >10%.',
                'Dominated by herbaceous annuals (<2m). At least 60% ' +
                'cultivated broadleaf crops.',
                'Dominated by herbaceous annuals (<2m) including cereal ' +
                'croplands.',
                'At least 60% of area is non-vegetated barren (sand, rock, ' +
                'soil) or permanent snow/ice with less than 10% vegetation.',
                'At least 30% impervious surface area including building ' +
                'materials, asphalt, and vehicles.',
                'Has not received a map label because of missing inputs.']}
table6 = pd.DataFrame(data=d)

# Plant Functional Types (PFT) legend and class denitions.
d = {
'Name': ['Water Bodies', 'Evergreen Needleleaf Trees',
         'Evergreen Broadleaf Trees', 'Deciduous Needleleaf Trees',
         'Deciduous Broadleaf Trees', 'Shrub', 'Grass', 'Cereal Croplands',
         'Broadleaf Croplands', 'Urban and Built-up Lands',
         'Permanent Snow and Ice', 'Barren', 'Unclassified'],
'Value': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '255'],
'Description': ['At least 60% of area is covered by permanent water bodies.',
                'Dominated by evergreen conifer trees (>2m). Tree cover >10%.',
                'Dominated by evergreen broadleaf and palmate trees (>2m). ' +
                'Tree cover >10%.',
                'Dominated by deciduous needleleaf (larch) trees (>2m). ' +
                'Tree cover >10%.',
                'Dominated by deciduous broadleaf trees (>2m). Tree cover ' +
                '>10%.',
                'Shrub (1-2m) cover >10%.',
                'Dominated by herbaceous annuals (<2m) that are not ' +
                'cultivated.',
                'Dominated by herbaceous annuals (<2m). At least 60% ' +
                'cultivated cereal crops.',
                'Dominated by herbaceous annuals (<2m). At least 60% ' +
                'cultivated broadleaf crops.',
                'At least 30% impervious surface area including building ' +
                'materials, asphalt, and vehicles.',
                'At least 60% of area is covered by snow and ice for at ' +
                'least 10 months of the year.',
                'At least 60% of area is non-vegetated barren (sand, rock, ' +
                'soil) with less than 10% vegetation.',
                'Has not received a map label because of missing inputs.']}
table7 = pd.DataFrame(data=d)

# FAO-Land Cover Classification System land cover (LCCS1) legend and class 
# definitions.
d = {
'Name': ['Barren', 'Permanent Snow and Ice', 'Water Bodies',
         'Evergreen Needleleaf Forests', 'Evergreen Broadleaf Forests',
         'Deciduous Needleleaf Forests', 'Deciduous Broadleaf Forests',
         'Mixed Broadleaf/Needleleaf Forests',
         'Mixed Broadleaf Evergreen/Deciduous Forests',
         'Open Forests', 'Sparse Forests', 'Dense Herbaceous',
         'Sparse Herbaceous', 'Dense Shrublands', 'Shrubland/Grassland Mosaics',
         'Sparse Shrublands', 'Unclassified'],
'Value': ['1', '2', '3', '11', '12', '13', '14', '15', '16', '21', '22', '31',
          '32', '41', '42', '43', '255'],
'Description': ['At least of area 60% is non-vegetated barren (sand, rock, ' +
                'soil) or permanent snow/ice with less than 10% vegetation.',
                'At least of area 60% is covered by snow and ice for at ' +
                'least 10 months of the year.',
                'At least 60% of area is covered by permanent water bodies.',
                'Dominated by evergreen conifer trees (>2m). Tree cover >60%.',
                'Dominated by evergreen broadleaf and palmate trees (>2m). ' +
                'Tree cover >60%.',
                'Dominated by deciduous needleleaf (larch) trees (>2m). ' +
                'Tree cover >60%.',
                'Dominated by deciduous broadleaf trees (>2m). Tree cover ' +
                '>60%.',
                'Co-dominated (40-60%) by broadleaf deciduous and evergreen ' +
                'needleleaf tree (>2m) types. Tree cover >60%.',
                'Co-dominated (40-60%) by broadleaf evergreen and deciduous ' +
                'tree (>2m) types. Tree cover >60%.',
                'Tree cover 30-60% (canopy >2m).',
                'Tree cover 10-30% (canopy >2m).',
                'Dominated by herbaceous annuals (<2m) at least 60% cover.',
                'Dominated by herbaceous annuals (<2m) 10-60% cover.',
                'Dominated by woody perennials (1-2m) >60% cover.',
                'Dominated by woody perennials (1-2m) 10-60% cover with ' +
                'dense herbaceous annual understory.',
                'Dominated by woody perennials (1-2m) 10-60% cover with ' +
                'minimal herbaceous understory.',
                'Has not received a map label because of missing inputs.']}
table8 = pd.DataFrame(data=d)

# FAO-Land Cover Classification System land use (LCCS2) legend and class 
# definitions.
d = {
'Name': ['Barren', 'Permanent Snow and Ice', 'Water Bodies',
         'Urban and Built-up Lands', 'Dense Forests', 'Open Forests',
         'Forest/Cropland Mosaics', 'Natural Herbaceous',
         'Natural Herbaceous/Croplands Mosaics', 'Herbaceous Croplands',
         'Shrublands', 'Unclassified'],
'Value': ['1', '2', '3', '9', '10', '20', '25', '30', '35', '36', '40', '255'],
'Description': ['At least 60% of area is non-vegetated barren (sand, rock, ' +
                'soil) or permanent snow/ice with less than 10% vegetation.',
                'At least 60% of area is covered by snow and ice for at ' +
                'least 10 months of the year.',
                'At least 60% of area is covered by permanent water bodies.',
                'At least 30% of area is made up of impervious surfaces ' +
                'including building materials, asphalt, and vehicles.',
                'Tree cover >60% (canopy >2m).',
                'Tree cover 10-60% (canopy >2m).',
                'Mosaics of small-scale cultivation 40-60% with >10% ' +
                'natural tree cover.',
                'Dominated by herbaceous annuals (<2m). At least 10% cover.',
                'Mosaics of small-scale cultivation 40-60% with natural ' +
                'shrub or herbaceous vegetation.',
                'Dominated by herbaceous annuals (<2m). At least 60% cover. ' +
                'Cultivated fraction >60%.',
                'Shrub cover >60% (1-2m).',
                'Has not received a map label because of missing inputs.']}
table9 = pd.DataFrame(data=d)

# FAO-Land Cover Classification System surface hydrology (LCCS3) legend and 
# class descriptions.
d = {
'Name': ['Barren', 'Permanent Snow and Ice', 'Water Bodies',
         'Dense Forests', 'Open Forests', 'Woody Wetlands', 'Grasslands',
         'Shrublands', 'Herbaceous Wetlands', 'Tundra', 'Unclassified'],
'Value': ['1', '2', '3', '10', '20', '27', '30', '40', '50', '51', '255'],
'Description': ['At least 60% of area is non-vegetated barren (sand, rock, ' +
                'soil) or permanent snow/ice with less than 10% vegetation.',
                'At least 60% of area is covered by snow and ice for at ' +
                'least 10 months of the year.',
                'At least 60% of area is covered by permanent water bodies.',
                'Tree cover >60% (canopy >2m).',
                'Tree cover 10-60% (canopy >2m).',
                'Shrub and tree cover >10% (>1m). Permanently or seasonally ' +
                'inundated',
                'Dominated by herbaceous annuals (<2m) >10% cover.',
                'Shrub cover >60% (1-2m).',
                'Dominated by herbaceous annuals (<2m) >10% cover. ' +
                'Permanently or seasonally inundated.',
                'Tree cover <10%. Snow-covered for at least 8 months of the ' +
                'year.',
                'Has not received a map label because of missing inputs.']}
table10 = pd.DataFrame(data=d)

# Quality Assurance (QA) legend and class descriptions.
d = {
'Name': ['Classified land', 'Unclassified land', 'Classified water',
         'Unclassified water', 'Classified sea ice', 'Misclassified water',
         'Omitted snow/ice', 'Misclassified snow/ice', 'Backfilled label',
         'Forest type changed', 'No data'],
'Value': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
'Description': ['Has a classification label and is land according to the ' +
                'water mask.',
                'Not classified because of missing data but land according ' +
                'to the water mask, labeled as barren.',
                'Has a classification label and is water according to the ' +
                'water mask.',
                'Not classified because of missing data but water according ' +
                'to the water mask.',
                'Classified as snow/ice but water mask says it is water and ' +
                'less than 100m elevation, switched to water.',
                'Classified as water but water mask says it is land, ' +
                'switched to secondary label.',
                'Land according to the water mask that was classified as ' +
                'something other than snow but with a maximum annual ' +
                'temperature below 1' + chr(176) + 'C, relabeled as snow/ice.',
                'Land according to the water mask that was classified as ' +
                'snow but with a minimum annual temperature greater than ' +
                '1' + chr(176) + 'C, relabeled as barren.',
                'Missing label from stabilization, filled with the ' +
                'pre-stabilized result.',
                'Climate-based change to forest class.',
                'Missing label from the water mask.']}
table11 = pd.DataFrame(data=d)

# MCD12C1 International Geosphere-Biosphere Programme (IGBP) legend and class
# descriptions.
# The other class legends of the MCD12C1 product are identical to the MCD12Q1
# product above.
d = {
'Name': ['Water Bodies',
          'Evergreen Needleleaf Forests', 'Evergreen Broadleaf Forests',
          'Deciduous Needleleaf Forests','Deciduous Broadleaf Forests',
          'Mixed Forests', 'Closed Shrublands', 'Open Shrublands',
          'Woody Savannas', 'Savannas', 'Grasslands', 'Permanent Wetlands',
          'Croplands', 'Urban and Built-up Lands',
          'Cropland/Natural Vegetation Mosaics', 'Permanent Snow and Ice',
          'Barren', 'Unclassified'],
'Value': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
          '13', '14', '15', '16', '255'],
'Description': ['At least 60% of area is covered by permanent water bodies.',
                'Dominated by evergreen conifer trees (canopy>2m). ' +
                'Tree cover >60%.',
                'Dominated by evergreen broadleaf and ' +
                'palmatetrees (canopy >2m). Tree cover >60%.',
                'Dominated by deciduous needleleaf (larch) trees ' +
                '(canopy >2m). Tree cover >60%.',
                'Dominated by deciduous broadleaf trees (canopy>2m). ' +
                'Tree cover >60%.',
                'Dominated by neither deciduous nor evergreen (40-60% ' +
                'of each) tree type (canopy >2m). Treecover >60%.',
                'Dominated by woody perennials (1-2m height) >60% cover.',
                'Dominated by woody perennials (1-2m height) 10-60% cover.',
                'Tree cover 30-60% (canopy >2m).',
                'Tree cover 10-30% (canopy >2m).',
                'Dominated by herbaceous annuals (<2m).',
                'Permanently inundated lands with 30-60% water cover and ' +
                '>10% vegetated cover.',
                'At least 60% of area is cultivated cropland.',
                'At least 30% impervious surface area including building ' +
                'materials, asphalt, and vehicles.',
                'Mosaics of small-scale cultivation 40-60% with natural ' +
                'tree, shrub, or herbaceous vegetation.',
                'At least 60% of area is covered by snow and ice for at ' +
                'least 10 months of the year.',
                'At least 60% of area is non-vegetated barren (sand, rock, ' +
                'soil) areas with less than 10% vegetation.',
                'Has not received a map label because of missing inputs.']}
table12 = pd.DataFrame(data=d)

#put dataframes in an array and return array
def MCD12_user_guide():
    return [table1, table2, table3, table4, table5, table6, table7, table8,
            table9, table10, table11, table12]