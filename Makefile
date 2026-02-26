install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

test:
	uv run pytest tests/ -v

.PHONY: install brain-games brain-even brain-calc brain-gcd brain-progression brain-prime build package-install lint test