# Build package and test deployment to testpypi repo:
```bash
poetry build
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish -r testpypi

```
