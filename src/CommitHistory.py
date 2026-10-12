from helper.cmd import CMD
class CommitHistory:
    def __init__(self, provider, repo_url, github_token, gitlab_token):
        self.repo_provider = provider 
        self.repo_url = repo_url
        self.github_token = github_token
        self.gitlab_token = gitlab_token
        self.cmd = CMD()
        self.commit_history = ""

    def get_repo_commit_history(self):
        if(self.repo_provider == "github"):
            self.commit_history = self.cmd.run_cmd(f"curl -L -H \"Accept: application/vnd.github+json -H \"Authorization: Bearer {self.github_token}\" -H \"X-GitHub-Api-Version: 2026-03-10\" {self.repo_url}")
        else:
            self.commit_history = self.cmd.run_cmd(f"curl --header \"PRIVATE-TOKEN: {self.gitlab_token}\" --url \"{self.repo_url}\"") 
    
