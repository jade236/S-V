import os

def main():
  print("Hello from GitHub Actions!")
  token = os.environ.get("AZURE_SECRET_TOKEN")
  if not token:
    raise RuntimeError("AZURE_SECRET_TOKEN env var is not set!")
  print("All good! we found our env var")
 secret = os.getenv("AZURE_SECRET_TOKEN")
 print(f"ENV VARIABLE: {secret}")
  

if __name__ == '__main__':
  main()
