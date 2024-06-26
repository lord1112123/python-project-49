.PHONY: install
install:
	poetry install

.PHONY: brain-games
brain-games:
	poetry run brain-games

brain-calc:
    poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*whl

lint:
	poetry run flake8 brain_games
