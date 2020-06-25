# neptune

## Instalation

```cmd
pip install neptune-client

# or

conda install -c conda-forge neptune-client
```

### Set enviroment variable



## Using it (simple usage)

```python
neptune.init("user/projectname", api_toke="blablabla")

neptune.create_experiment()
neptune.append_tag('minimal-example')

n = 250

for i in range(1, n):
    neptune.send_metric('iteration', i)
    neptune.send_metric('loss', 1/i**0.5)
    neptune.set_property('n_iterations', n)
```

## Create an experiment

```python
# select project
neptune.init('user/mycoolproject')

neptune.create_experiment(name="my-cool-experimentname",
                          description="It's my cool experiment description",
			  tags=['example', 'test'],
			  params=PARAMS)

```

# Referências

[neptune docs](https://docs.neptune.ai)
