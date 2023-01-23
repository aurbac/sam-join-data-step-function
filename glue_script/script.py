import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME","source1","source2","jobid"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customers
Customers_node1674411976085 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={"paths": [args["source1"]], "recurse": True},
    transformation_ctx="Customers_node1674411976085",
)

# Script generated for node Locations
Locations_node1674411977700 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={"paths": [args["source2"]], "recurse": True},
    transformation_ctx="Locations_node1674411977700",
)

# Script generated for node Join
Join_node1674412127524 = Join.apply(
    frame1=Locations_node1674411977700,
    frame2=Customers_node1674411976085,
    keys1=["zipcode"],
    keys2=["zipcode"],
    transformation_ctx="Join_node1674412127524",
)

# Script generated for node Change Schema (Apply Mapping)
ChangeSchemaApplyMapping_node1674412168807 = ApplyMapping.apply(
    frame=Join_node1674412127524,
    mappings=[
        ("zipcode", "string", "zipcode", "string"),
        ("country", "string", "country", "string"),
        ("state", "string", "state", "string"),
        ("id", "string", "id", "string"),
        ("name", "string", "name", "string"),
        ("value", "string", "value", "string"),
        ("`.zipcode`", "string", "`.zipcode`", "string"),
    ],
    transformation_ctx="ChangeSchemaApplyMapping_node1674412168807",
)

# Script generated for node Amazon S3
AmazonS3_node1674412223396 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchemaApplyMapping_node1674412168807,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://site.aurbac.com/output/"+args["jobid"]+"/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1674412223396",
)

job.commit()
