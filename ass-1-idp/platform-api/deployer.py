import subprocess

def deploy_app(app_name, image, environment):
    try:
        image_repo, image_tag = image.split(":")

        command = [
            "helm", "upgrade", "--install", app_name,
            "../helm/app-chart",
            "-n", environment,
            "-f", f"../helm/app-chart/values-{environment}.yaml",
            "--set", f"appName={app_name}",
            "--set", f"image.repository={image_repo}",
            "--set", f"image.tag={image_tag}"
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            return {"status": "error", "message": result.stderr}

        return {
            "status": "success",
            "message": f"{app_name} deployed successfully in {environment}"
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}