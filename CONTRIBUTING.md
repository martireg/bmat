# Contributing
We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## We Develop with Github
We use github to host code, to track issues and feature requests, as well as accept pull requests.

## We Use [Github Flow](https://guides.github.com/introduction/flow/index.html), So All Code Changes Happen Through Pull Requests
Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://guides.github.com/introduction/flow/index.html)). We actively welcome your pull requests:

1. Fork the repo and create your branch from `master`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation. (eg swagger)
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Any contributions you make will be under the MIT Software License
In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using Github's [issues](https://github.com/briandk/transcriptase-atom/issues)
We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/martireg/bmat/issues/new/); it's that easy!

## Virtual environment

Use `pipenv shell` for starting and entering a venv.

## Test everything

All piece of software must come with it's own piece of test suite
Be sure that all tests are passing  `make test` and `make test-local`
Use `make lint` for code linting

## Use a Consistent Coding Style

* 4 spaces for indentation rather than tabs
* double quotes "" rather than single quotes ''
* You can try running `pipenv run black .` for style unification
* Use type hints when possible

## License
By contributing, you agree that your contributions will be licensed under its MIT License.
