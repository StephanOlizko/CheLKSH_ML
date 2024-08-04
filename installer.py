import os
import subprocess
import sys
from pathlib import Path

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package {package}: {e}")
        sys.exit(1)

def clone_repository(repo_url, clone_dir):
    try:
        import git
    except ImportError:
        print("gitpython not installed. Installing it now.")
        install_package("gitpython")
        import git

    try:
        if not os.path.exists(clone_dir):
            print(f"Cloning repository from {repo_url} to {clone_dir}")
            git.Repo.clone_from(repo_url, clone_dir)
        else:
            print(f"Repository already cloned in {clone_dir}")
    except Exception as e:
        print(f"An error occurred while cloning the repository: {e}")
        sys.exit(1)

def install_requirements(clone_dir):
    requirements_path = os.path.join(clone_dir, "requirements.txt")
    if os.path.exists(requirements_path):
        print(f"Installing requirements from {requirements_path}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install requirements: {e}")
            sys.exit(1)
    else:
        print(f"requirements.txt not found in {clone_dir}")

def get_clone_directory():
    if os.name == 'nt':  # Windows
        documents_dir = Path.home() / "Documents"
        clone_dir = documents_dir / "my_cloned_repo"
    else:  # Unix-like system
        home_dir = Path.home()
        clone_dir = home_dir / "my_cloned_repo"
    
    return str(clone_dir)

if __name__ == "__main__":
    # URL репозитория
    repo_url = "https://github.com/your/repository.git"
    # Определение пути для клонирования в зависимости от ОС
    clone_dir = get_clone_directory()

    clone_repository(repo_url, clone_dir)
    install_requirements(clone_dir)
