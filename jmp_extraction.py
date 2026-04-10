import pandas as pd
# Load the dataset1
households_facility = pd.read_csv('/Users/kikoxu/Downloads/JMP/jmp_households_facility.csv')
print(households_facility.head())
print(households_facility.columns)

# Load the dataset2
households_service = pd.read_csv('/Users/kikoxu/Downloads/JMP/jmp_households_service.csv')
print(households_service.head())
print(households_service.columns)

# Load the dataset3
households_safely_managed = pd.read_csv('/Users/kikoxu/Downloads/JMP/jmp_households_safely_managed.csv')
print(households_safely_managed.head())
print(households_safely_managed.columns)

# Load the dataset4
schools_service = pd.read_csv('/Users/kikoxu/Downloads/JMP/jmp_schools_service.csv')
print(schools_service.head())
print(schools_service.columns)

# Load the dataset5
healthcare_service = pd.read_csv('/Users/kikoxu/Downloads/JMP/jmp_healthcare_service.csv')
print(healthcare_service.head())
print(healthcare_service.columns)

# Add column for Sector
households_facility["Sector"] = "Households"
households_service["Sector"] = "Households"
households_safely_managed["Sector"] = "Households"
schools_service["Sector"] = "Schools"
healthcare_service["Sector"] = "Healthcare"

# Rename Columns for Merging
households_facility = households_facility.rename(columns={"Residence Type": "Residence/Schools/Facility Type"})
households_service = households_service.rename(columns={"Residence Type": "Residence/Schools/Facility Type"})
households_safely_managed = households_safely_managed.rename(columns={"Residence Type": "Residence/Schools/Facility Type"})
schools_service = schools_service.rename(columns={"Residence / School Type": "Residence/Schools/Facility Type"})
healthcare_service = healthcare_service.rename(columns={"Residence / Facility Type": "Residence/Schools/Facility Type"})
schools_service = schools_service.rename(columns={"School-age population": "Population"})

#Merge Datasets
jmp_data = pd.concat([households_facility, households_service, households_safely_managed, schools_service, healthcare_service])

#Rename and Reorganize Columns
jmp_data = jmp_data.rename(columns={"Facility type": "Facility Type"})
jmp_data = jmp_data.rename(columns={"Service level": "Service Level"})
jmp_data = jmp_data.rename(columns={"Safely managed element": "Safely Managed Element"})
jmp_data = jmp_data[['ISO3', 'Country', 'Year', 'Sector', 'Residence/Schools/Facility Type', 'Service Type', 'Service Level', 'Facility Type', 'Safely Managed Element', 'Population', 'Coverage']]

output_path = '/Users/kikoxu/Downloads/JMP/jmp_data.csv'
jmp_data.to_csv(output_path, index=False)

output_path