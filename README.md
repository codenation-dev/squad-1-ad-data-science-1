# [`recommender_system_squad_1`]
> Simple project description.

This model is a `recommender_system` that `suggest new customers` based on a database with more than 460 000 clients. This base you can download [here](https://drive.google.com/open?id=1HUThfBgS3ZpdqoVu1mbxjSVjkCGKHkZg) and paste in this git folder. The notebook file ` Recommendation_system.ipynb` is running the recommendation system and use `clientes2_merge.csv` as example.

## Stakeholders
> Describe the people involved in this project

| Role                 | Responsibility         | Full name                | e-mail       |
| -----                | ----------------       | -----------              | ---------    |
| Data Scientist       | Author                 | [`bruno-manoel-dbki`]            | [`brunomanoel@dobrovolski.com.br`] |
| Data Scientist       | Author              | [`Fernando Santana Pacheco`] | [`fspacheco@gmail.com`]   |

## Usage
> Describe how to reproduce your model

Usage is standardized across models. There are two main things you need to know, the development workflow and the Makefile commands.

Both are made super simple to work with Git and Docker while versioning experiments and workspace.

All you'll need to have setup is Docker and Git, which you probably already have. If you don't, feel free to ask for help.

Makefile commands can be accessed using `make help`.


Make sure that **docker** is installed.

Clone the project from the analytics Models repo.
```
git clone https://github.com/<@github_username>/recommender_system_squad_1.git
cd recommender_system_squad_1
```


## Final Report (to be filled once the project is done)

### Model Frequency

> Describe the interval frequency and estimated total time to run

### Model updating

> Describe how your model may be updated in the future

### Maintenance

> Describe how your model may be maintained in the future

### Minimum viable product

> Describe a minimum configuration that would be able to create a minimum viable product.

### Early adopters

> Describe any potential paying users for this product if it was available today. Also state a point of contact for each of them.

## Documentation

* [project_specification.md](./docs/project_specification.md): gives a data-science oriented description of the project.

* [model_report.md](./docs/model_report.md): describes the modeling performed.


#### Folder structure
>Explain you folder strucure

* [docs](./docs): contains documentation of the project
* [analysis](./analysis/): contains notebooks of data and modeling experimentation.
* [tests](./tests/): contains files used for unit tests.
* [recommender_system_squad_1](./recommender_system_squad_1/): main Python package with source of the model.
