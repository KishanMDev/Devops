# Exercise 8: Creating "Hello World" Jenkins Automated Job

## Objective
Author a custom automation shell script (`hello-world.sh`), configure Git version control tracking, and integrate it into Jenkins as an automated pipeline build job. This exercise demonstrates how Jenkins agents check out repository code, grant execution permissions, execute shell steps, and capture console logs with success indicators.

## Workflow
1. **Local Authoring**: Author `hello-world.sh` and make executable.
2. **Git Version Control**: Track script in local Git repository and create clean commit history.
3. **Jenkins Job Configuration**: Configure a Jenkins Pipeline job linked to the repository.
4. **Build Execution**: Trigger Build #1 and verify console output.

## Files Included
- `hello-world.sh`: Executable bash automation script
- `Jenkinsfile`: Declarative pipeline orchestration script
- `screenshots/`: Execution proof captures

## Execution Steps
1. **Create and Test Shell Script Locally**:
   ```bash
   chmod +x hello-world.sh
   ./hello-world.sh
   ```
2. **Commit Script to Repository**:
   ```bash
   git add hello-world.sh Jenkinsfile
   git commit -m "feat: Add hello-world.sh Jenkins automation script"
   ```
3. **Configure & Trigger Jenkins Job**:
   Configure Pipeline job `Jenkins-Hello-World` and trigger `Build Now`.
4. **Inspect Console Output**:
   Verify console log reflects exit code 0 and `SUCCESS`.

## Execution Proof (Screenshots)
- `screenshots/01-git-commit-hello-world.png`: Git commit and file status verification
- `screenshots/02-jenkins-job-configuration.png`: Pipeline script syntax and job setup
- `screenshots/03-jenkins-console-output-success.png`: Console output demonstrating script execution and `Finished: SUCCESS`
