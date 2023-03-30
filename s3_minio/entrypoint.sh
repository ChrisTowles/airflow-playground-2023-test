#!/bins/sh

# NOTE to test this script, run the following command:
# docker compose up locals3 locals3_init --build


echo "INPUT_BUCKETS=$INPUT_BUCKETS"
echo "COPY_DIR=$COPY_DIR"

while ! /usr/bin/mc config host add locals3 http://locals3:9000 $USER $PASSWORD;
  do echo 'MinIO not up and running yet...' && sleep 1;
done;

echo 'Added mc host config.';

echo "Variable COPY_DIR is set to $COPY_DIR"
 
/usr/bin/mc mb locals3/datalake
#/usr/bin/mc cp --recursive ~/mydata/ locals3/datalake

echo "test file" > test.txt
/usr/bin/mc cp ./test.txt locals3/datalake/test.txt

echo "Created datalake s3 bucket and entry"

/usr/bin/mc admin user add locals3 FAKEACCESSKEY V7f1CwQqAcwo80UEIJEjc5gVQUSSx5ohQ9GSrr12
#/usr/bin/mc admin policy set locals3 readwrite user=ACCESSKEY
/usr/bin/mc admin policy attach locals3 readwrite --user=FAKEACCESSKEY
echo "Created user and policy"


/usr/bin/mc admin user add locals3 airflow airflow_secret;
echo 'Added user airflow.';
/usr/bin/mc admin policy set locals3 readwrite user=airflow;
/usr/bin/mc mb locals3/data;
/usr/bin/mc alias set locals3 http://locals3 9RTK1ISXS13J85I4U6JS 4z+akfubnu+XZuoCXhqGwrtq+jgK2AYcrgGH5zsQ --api s3v4;
exit 0;