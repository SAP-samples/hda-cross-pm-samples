# Preparations before workshop

## Tables in HANA Cloud

### Create Schema
```
CREATE SCHEMA DSP_WORKSHOP_GASPRICES;
```

### GAS_PRICES
```
CREATE COLUMN TABLE "DSP_WORKSHOP_GASPRICES"."GAS_PRICES"(
	"DATE" LONGDATE NOT NULL,
	"STATION_UUID" NVARCHAR(50) NOT NULL,
	"DIESEL" DOUBLE,
	"E5" DOUBLE,
	"E10" DOUBLE,
	"DIESELCHANGE" INTEGER,
	"E5CHANGE" INTEGER,
	"E10CHANGE" INTEGER,
	PRIMARY KEY INVERTED INDIVIDUAL(
		"DATE",
		"STATION_UUID"
	)
)
```

### GAS_STATIONS
```
CREATE COLUMN TABLE "DSP_WORKSHOP_GASPRICES"."GAS_STATIONS"(
	"uuid" NVARCHAR(50) NOT NULL,
	"name" NVARCHAR(300),
	"brand" NVARCHAR(300),
	"street" NVARCHAR(50),
	"house_number" NVARCHAR(50),
	"post_code" NVARCHAR(50),
	"city" NVARCHAR(50),
	"latitude" NVARCHAR(50),
	"longitude" NVARCHAR(50),
	"first_active" NVARCHAR(50),
	"openingtimes_json" NVARCHAR(3000),
	PRIMARY KEY(
		"uuid"
	)
)
```

## Data available in https://dev.azure.com/tankerkoenig/_git/tankerkoenig-data
Run the following script in the folder containing the gas station prices to create one CSV.
```
import pandas as pd
 
df_csv_append = pd.DataFrame()
 
# append the CSV files
for file in csv_files:
    df = pd.read_csv(file)
    df_csv_append = df_csv_append._append(df, ignore_index=True)
 
df_csv_append.to_csv('allcsvs.csv',sep=',', index=False)
```

## Create user

```
CREATE USER HC_PARTNER PASSWORD "SETPASSWORD" NO FORCE_FIRST_PASSWORD_CHANGE;
GRANT SELECT ON SCHEMA DSP_WORKSHOP_GASPRICES TO HC_PARTNER;
ALTER USER HC_PARTNER REVOKE CREATE ANY ON OWN SCHEMA;
```

### Deactive "lock" mechanism for technical user

```
-- create user group
CREATE USERGROUP UnlockableUser SET PARAMETER 'password_lock_time' = '0' ENABLE PARAMETER SET 'password policy';

-- assign user group to user
ALTER USER HC_PARTNER SET USERGROUP UnlockableUser;
```