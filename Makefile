.PHONY: install brain-games

install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

.PHONY: lint

lint:
	uv run ruff check brain_games
	