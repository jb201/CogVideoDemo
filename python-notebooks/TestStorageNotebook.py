# Databricks notebook source
# We should store this in a databrick secret 
mounts = dbutils.fs.mounts()
mountPoint = next((x for x in mounts if x.mountPoint == '/mnt/v/'), None)
print (mountPoint)
sasToken = '?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-12-01T23:26:30Z&st=2019-06-28T14:26:30Z&spr=https&sig=xxxxxx'


if mountPoint == None:
  dbutils.fs.mount(source = 'wasbs://BLOBCONTAINERNAME@STORAGEACCOUNTNAME.blob.core.windows.net',mount_point = '/mnt/v/', extra_configs = {'fs.azure.sas.BLOBCONTAINERNAME.STORAGEACCOUNTNAME.blob.core.windows.net': sasToken})
  
# If you need to unmount to refresh keys do htis
# dbutils.fs.unmount(mount_point = '/mnt/v/')


# COMMAND ----------


dbutils.fs.ls("/mnt/v/")
