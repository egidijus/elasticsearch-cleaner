# python tool to delete indexes from elasticsearch older than specified date, this is for older ES, because new ES supports index life cycle management via kibana.

Because this is a destructive tool, I decided to start with a test that
 would create test data based on a pattern.
This way, you would use the same code to "target" what indexes you create,
 as the code that you use to "target" which indexes you want to delete.

Hopefully you will know that only the indexes you are intending to delete will be deleted.

This is a python3 tool, you will need some packages to get started.
I am expecting you to have installed:
```
make
virtualenv
python3
pip
```

For testing, you will need to run a local copy of elasticsearch,
try using this to start an all in one *docker* image with kibana,
elasticsearch and logstash
(we are only interested in elasticsearch and kibana for looking at what happens to our indexes).
The below command will run a container in the foreground, you will need to open another terminal window to proceed.
```
docker run -it --rm -p 5601:5601 -p 9200:9200 -p 9300:9300 -e LOGSTASH_START=nope sebp/elk:es241_l240_k461
```


The `Makefile` has some targets that will:
1. Setup your local environment with virtualenv.
1. Install python requirements.
1. Run the tests to create indexes, delete indexes and verify only desired indexes were deleted.


Firstly lets setup the local environment.
To install all the dependencies and get ready to run, do this:
```
make build
```

While you have a local elasticsearch running, write a sample dataset.
This does not yet test if you deleted the intended indexes, that is coming next:
```
make test
```

