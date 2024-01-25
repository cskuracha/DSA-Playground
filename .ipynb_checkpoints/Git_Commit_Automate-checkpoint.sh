#!/bin/sh
cd /Workspace/PythonWorkspace/Practice/DSA-Playground
git add --all
timestamp() {
  date +"at %H:%M:%S on %d/%m/%Y"
}
git commit -am "Auto-commit $(timestamp)"
git push origin main