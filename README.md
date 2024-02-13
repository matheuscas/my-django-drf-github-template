# One more Django + DRF starter (template).
An highly optioned Django + DRF Github template (always evolving)

Why? Because I can. :)
Kidding. Not Kidding. Learning purposes also.

As of we have:

### Package manager

[Poetry](https://python-poetry.org/)

### [Pre-commit](https://pre-commit.com/) hooks

  - ruff
  - ruff-format
  - isort
  - mypy
  - pyupgrade
  - commitizen (commit-msg)

### Commit message linter, semVer control, etc.

[Commitizen](https://commitizen-tools.github.io/commitizen/)

### Github actions

- [Testing](https://github.com/matheuscas/my-django-drf-github-template/blob/main/.github/workflows/testing.yaml)
- [Code linting and formatting check](https://github.com/matheuscas/my-django-drf-github-template/blob/main/.github/workflows/linting_formating.yaml)
- [Migrations linting](https://github.com/3YOURMIND/django-migration-linter?tab=readme-ov-file)

### OpenApi Documentation

[drf-Spectacular](https://github.com/tfranzel/drf-spectacular)

### Testing

- [pytest](https://docs.pytest.org/en/7.4.x/)
- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
- [mixer](https://github.com/klen/mixer)

### User base model

[User model extended from AbstractUser](https://testdriven.io/blog/django-custom-user-model/) to use
email instead of the username.
