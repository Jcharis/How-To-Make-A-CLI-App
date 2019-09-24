from click.testing import CliRunner
from simple_cli import main

# Unit Test

def test_say_in_cli():
	runner = CliRunner()
	result = runner.invoke(main,['say','Hello'])
	assert 'You said Hello' in result.output
	assert result.exit_code == 0


def test_greet_in_cli():
	runner = CliRunner()
	result = runner.invoke(main,['greet','John'])
	assert result.output == 'Hello John\n'
	assert result.exit_code == 0
