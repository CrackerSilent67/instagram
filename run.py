import sys, os


if __name__ == "__main__":
  try:
      os.system("git pull")
      __import__("instagram").checkin()
  except Exception as e:
    exit(str(e))
