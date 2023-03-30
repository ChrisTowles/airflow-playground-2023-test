#!/bins/sh

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
