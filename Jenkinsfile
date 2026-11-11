pipeline {
    agent any

    stages {
        stage('Preparar entorno') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Revisar estilo') {
            steps {
                sh '.venv/bin/python -m flake8 calculadora.py test_calculadora.py'
            }
        }

        stage('Pruebas') {
            steps {
                sh '.venv/bin/python -m pytest --junitxml=reporte-pruebas.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reporte-pruebas.xml'
        }
        success {
            echo 'Todo en verde: el cambio se puede integrar.'
        }
        failure {
            echo 'Build roto: revisa la salida de consola y el reporte de pruebas.'
        }
    }
}
