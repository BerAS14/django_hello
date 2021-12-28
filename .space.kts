/**
* JetBrains Space Automation
* This Kotlin-script file lets you automate build activities
* For more info, see https://www.jetbrains.com/help/space/automation.html
*/

job("python unittests") {
    container(displayName = "python:3.9", image = "python:3.9-slim-bullseye"){
        shellScript {
            content = """
                python -m unittest discover -p test_*.py

                pip install pipenv
                pipenv sync --system
                python manage.py migrate
            """
        }
    }
}
