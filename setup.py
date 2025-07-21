#!/usr/bin/env python3
"""
Universal Claude Code Container Setup Script

This script guides users through the complete setup process for the
Universal Claude Code Container, including IDE configuration, MCP servers,
API keys, and container deployment.

Author: Claude Code Assistant
Version: 1.0.0
License: MIT
"""

import os
import sys
import json
import platform
import subprocess
import shutil
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import urllib.request
import webbrowser

# ANSI color codes for terminal output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class UniversalContainerSetup:
    def __init__(self):
        self.system = platform.system().lower()
        self.home_dir = Path.home()
        self.script_dir = Path(__file__).parent
        self.config = {}
        self.claude_config_path = self.get_claude_config_path()
        
        # MCP Server configurations
        self.mcp_servers = {
            'github': {
                'name': 'GitHub',
                'description': 'GitHub API integration for repositories, issues, PRs',
                'command': 'npx',
                'args': ['-y', '@modelcontextprotocol/server-github'],
                'env_vars': ['GITHUB_PERSONAL_ACCESS_TOKEN'],
                'setup_url': 'https://github.com/settings/tokens'
            },
            'filesystem': {
                'name': 'File System',
                'description': 'Advanced file operations beyond standard Claude Code access',
                'command': 'node',
                'args': [],  # Will be set dynamically
                'env_vars': [],
                'local_server': True
            },
            'sequential-thinking': {
                'name': 'Sequential Thinking',
                'description': 'Enhanced reasoning and problem-solving capabilities',
                'command': 'npx',
                'args': ['-y', '@modelcontextprotocol/server-sequential-thinking'],
                'env_vars': []
            },
            'puppeteer': {
                'name': 'Puppeteer',
                'description': 'Web automation, scraping, and browser control',
                'command': 'npx',
                'args': ['-y', 'puppeteer-mcp-server'],
                'env_vars': []
            },
            'postgres': {
                'name': 'PostgreSQL',
                'description': 'Direct PostgreSQL database interactions',
                'command': 'npx',
                'args': ['-y', '@modelcontextprotocol/server-postgres'],
                'env_vars': ['POSTGRES_CONNECTION_STRING']
            },
            'memory': {
                'name': 'Memory Bank',
                'description': 'Persistent memory across conversations',
                'command': 'npx',
                'args': ['-y', '@modelcontextprotocol/server-memory'],
                'env_vars': []
            },
            'context7': {
                'name': 'Context7',
                'description': 'Vector database for semantic search and contextual retrieval',
                'command': 'npx',
                'args': ['-y', '@upstash/context7'],
                'env_vars': ['UPSTASH_VECTOR_REST_URL', 'UPSTASH_VECTOR_REST_TOKEN'],
                'setup_url': 'https://console.upstash.com'
            },
            'notion': {
                'name': 'Notion',
                'description': 'Notion workspace integration via Composio',
                'command': 'npx',
                'args': ['@composio/mcp@latest', 'run', 'notion'],
                'env_vars': ['COMPOSIO_API_KEY'],
                'setup_url': 'https://app.composio.dev'
            },
            'figma': {
                'name': 'Figma',
                'description': 'Figma design integration via Composio',
                'command': 'npx',
                'args': ['@composio/mcp@latest', 'run', 'figma'],
                'env_vars': ['COMPOSIO_API_KEY'],
                'setup_url': 'https://app.composio.dev'
            },
            'zapier': {
                'name': 'Zapier',
                'description': 'Cross-app automation via Composio',
                'command': 'npx',
                'args': ['@composio/mcp@latest', 'run', 'zapier'],
                'env_vars': ['COMPOSIO_API_KEY'],
                'setup_url': 'https://app.composio.dev'
            },
            'apidog': {
                'name': 'Apidog',
                'description': 'API documentation and testing',
                'command': 'npx',
                'args': ['-y', '@modelcontextprotocol/server-http'],
                'env_vars': ['APIDOG_API_KEY'],
                'setup_url': 'https://apidog.com'
            }
        }

    def print_banner(self):
        """Print the setup banner"""
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║                    Universal Claude Code Container Setup                     ║
║                                                                              ║
║  🚀 The Perfect Development Environment for Any Project Type                 ║
║  🌐 Web • 📱 Mobile • 🔧 Backend • 🤖 ML • ☁️  DevOps                          ║
║                                                                              ║
║  Supports: JavaScript/TypeScript, Python, Go, Rust, Java, C++               ║
║  Mobile: Flutter, React Native, Android SDK, iOS tools                      ║
║  MCP Servers: 11 powerful integrations for Claude Code                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.END}
        """
        print(banner)

    def get_claude_config_path(self) -> Path:
        """Get the Claude Desktop configuration path for the current OS"""
        if self.system == 'windows':
            return Path(os.environ.get('APPDATA', '')) / 'Claude' / 'claude_desktop_config.json'
        elif self.system == 'darwin':  # macOS
            return self.home_dir / 'Library' / 'Application Support' / 'Claude' / 'claude_desktop_config.json'
        else:  # Linux
            return self.home_dir / '.config' / 'claude' / 'claude_desktop_config.json'

    def print_step(self, step_num: int, title: str, description: str = ""):
        """Print a step header"""
        print(f"\n{Colors.BLUE}{Colors.BOLD}{'='*80}{Colors.END}")
        print(f"{Colors.YELLOW}{Colors.BOLD}STEP {step_num}: {title}{Colors.END}")
        if description:
            print(f"{Colors.WHITE}{description}{Colors.END}")
        print(f"{Colors.BLUE}{'='*80}{Colors.END}\n")

    def print_success(self, message: str):
        """Print a success message"""
        print(f"{Colors.GREEN}✅ {message}{Colors.END}")

    def print_warning(self, message: str):
        """Print a warning message"""
        print(f"{Colors.YELLOW}⚠️  {message}{Colors.END}")

    def print_error(self, message: str):
        """Print an error message"""
        print(f"{Colors.RED}❌ {message}{Colors.END}")

    def print_info(self, message: str):
        """Print an info message"""
        print(f"{Colors.CYAN}ℹ️  {message}{Colors.END}")

    def wait_for_user(self, message: str = "Press Enter to continue..."):
        """Wait for user input"""
        input(f"\n{Colors.MAGENTA}{message}{Colors.END}")

    def ask_yes_no(self, question: str, default: bool = True) -> bool:
        """Ask a yes/no question"""
        default_str = "Y/n" if default else "y/N"
        response = input(f"{Colors.CYAN}{question} [{default_str}]: {Colors.END}").strip().lower()
        
        if not response:
            return default
        return response in ['y', 'yes', 'true', '1']

    def select_option(self, question: str, options: List[str], default: int = 0) -> int:
        """Let user select from a list of options"""
        print(f"\n{Colors.CYAN}{question}{Colors.END}")
        for i, option in enumerate(options):
            marker = ">" if i == default else " "
            print(f"  {marker} {i + 1}. {option}")
        
        while True:
            try:
                choice = input(f"\nEnter choice [1-{len(options)}] (default: {default + 1}): ").strip()
                if not choice:
                    return default
                choice_int = int(choice) - 1
                if 0 <= choice_int < len(options):
                    return choice_int
                else:
                    print(f"{Colors.RED}Invalid choice. Please enter 1-{len(options)}{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}Invalid input. Please enter a number.{Colors.END}")

    def check_prerequisites(self) -> bool:
        """Check if required tools are installed"""
        self.print_step(1, "Checking Prerequisites", "Verifying required tools are installed")
        
        required_tools = {
            'docker': 'Docker',
            'node': 'Node.js',
            'npm': 'npm',
            'git': 'Git'
        }
        
        missing_tools = []
        
        for tool, name in required_tools.items():
            try:
                result = subprocess.run([tool, '--version'], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    version = result.stdout.strip().split('\n')[0]
                    self.print_success(f"{name}: {version}")
                else:
                    missing_tools.append(name)
            except (subprocess.TimeoutExpired, FileNotFoundError):
                missing_tools.append(name)
        
        if missing_tools:
            self.print_error(f"Missing required tools: {', '.join(missing_tools)}")
            print(f"\n{Colors.YELLOW}Please install the missing tools and run this script again.{Colors.END}")
            print(f"{Colors.CYAN}Installation guides:{Colors.END}")
            print("• Docker: https://docs.docker.com/get-docker/")
            print("• Node.js: https://nodejs.org/")
            print("• Git: https://git-scm.com/downloads")
            return False
        
        self.print_success("All prerequisites are installed!")
        return True

    def select_ide(self) -> str:
        """Let user select their preferred IDE"""
        self.print_step(2, "IDE Selection", "Choose your preferred development environment")
        
        ides = [
            "VS Code (Recommended - Full container support)",
            "Android Studio (Mobile development)",
            "IntelliJ IDEA (Java/Kotlin/Scala projects)",
            "CLion (C/C++ projects)",
            "Visual Studio (Windows C++/.NET projects)",
            "PyCharm (Python development)",
            "WebStorm (Web development)",
            "Rider (C#/.NET development)",
            "GoLand (Go development)",
            "RustRover (Rust development)",
            "Eclipse (Java/C++ development)",
            "Neovim/Vim (Terminal-based)",
            "Emacs (Terminal/GUI-based)",
            "Sublime Text (Lightweight editor)",
            "Atom (GitHub's editor)",
            "Other IDE (Manual setup required)"
        ]
        
        choice = self.select_option("Which IDE do you primarily use?", ides, 0)
        ide_map = [
            'vscode', 'android_studio', 'intellij', 'clion', 'visual_studio',
            'pycharm', 'webstorm', 'rider', 'goland', 'rustrover',
            'eclipse', 'neovim', 'emacs', 'sublime', 'atom', 'other'
        ]
        return ide_map[choice]

    def setup_vscode(self):
        """Setup VS Code configuration"""
        print(f"\n{Colors.GREEN}Setting up VS Code with Dev Containers...{Colors.END}")
        
        extensions = [
            "ms-vscode-remote.remote-containers",
            "ms-vscode.remote-explorer",
            "GitHub.copilot",
            "GitHub.copilot-chat"
        ]
        
        print("Required VS Code extensions:")
        for ext in extensions:
            print(f"  • {ext}")
        
        if self.ask_yes_no("Would you like to install these extensions automatically?"):
            for ext in extensions:
                try:
                    subprocess.run(['code', '--install-extension', ext], 
                                 capture_output=True, check=True)
                    self.print_success(f"Installed {ext}")
                except subprocess.CalledProcessError:
                    self.print_warning(f"Could not install {ext} (install manually)")
        
        print(f"\n{Colors.CYAN}VS Code Setup Instructions:{Colors.END}")
        print("1. Open your project folder in VS Code")
        print("2. Copy the .devcontainer folder to your project root")
        print("3. When prompted, click 'Reopen in Container'")
        print("4. VS Code will build and start the container automatically")

    def setup_jetbrains(self, ide_type: str):
        """Setup JetBrains IDE configuration"""
        ide_names = {
            'android_studio': 'Android Studio',
            'intellij': 'IntelliJ IDEA',
            'clion': 'CLion',
            'pycharm': 'PyCharm',
            'webstorm': 'WebStorm',
            'rider': 'Rider',
            'goland': 'GoLand',
            'rustrover': 'RustRover'
        }
        
        ide_name = ide_names.get(ide_type, 'JetBrains IDE')
        print(f"\n{Colors.GREEN}Setting up {ide_name} with Docker integration...{Colors.END}")
        
        print(f"{Colors.CYAN}{ide_name} Setup Instructions:{Colors.END}")
        print("1. Install the Docker plugin in your IDE")
        print("2. Configure Docker connection (Settings → Docker)")
        print("3. Build the container: docker build -t universal-claude-container .")
        print("4. Run container with volume mounts for your project")
        print("5. Configure remote toolchain to use the container")
        
        # IDE-specific instructions
        if ide_type == 'clion':
            print(f"\n{Colors.YELLOW}CLion-specific steps:{Colors.END}")
            print("6. Set toolchain to Docker (Settings → Toolchains)")
            print("7. Configure CMake to use the Docker toolchain")
            print("8. Set CMake options: -G Ninja -DCMAKE_BUILD_TYPE=Debug")
        
        elif ide_type == 'android_studio':
            print(f"\n{Colors.YELLOW}Android Studio-specific steps:{Colors.END}")
            print("6. Configure Android SDK path: /opt/android-sdk")
            print("7. Set up Flutter SDK path: /opt/flutter")
            print("8. Configure Docker as build environment")
        
        elif ide_type == 'intellij':
            print(f"\n{Colors.YELLOW}IntelliJ IDEA-specific steps:{Colors.END}")
            print("6. Set Project SDK to container's Java installation")
            print("7. Configure Maven/Gradle to use container environment")
            print("8. Set up remote debugging if needed")
        
        elif ide_type == 'pycharm':
            print(f"\n{Colors.YELLOW}PyCharm-specific steps:{Colors.END}")
            print("6. Configure Python interpreter in container")
            print("7. Set up remote development server")
            print("8. Configure package management with pip/poetry in container")
        
        elif ide_type == 'webstorm':
            print(f"\n{Colors.YELLOW}WebStorm-specific steps:{Colors.END}")
            print("6. Configure Node.js interpreter in container")
            print("7. Set up npm/yarn/pnpm to use container environment")
            print("8. Configure debugging and testing frameworks")
        
        elif ide_type == 'rider':
            print(f"\n{Colors.YELLOW}Rider-specific steps:{Colors.END}")
            print("6. Configure .NET SDK in container")
            print("7. Set up NuGet package sources")
            print("8. Configure debugging and testing")
        
        elif ide_type == 'goland':
            print(f"\n{Colors.YELLOW}GoLand-specific steps:{Colors.END}")
            print("6. Configure Go SDK in container")
            print("7. Set GOPATH and GOROOT to container paths")
            print("8. Configure module proxy and testing")
        
        elif ide_type == 'rustrover':
            print(f"\n{Colors.YELLOW}RustRover-specific steps:{Colors.END}")
            print("6. Configure Rust toolchain in container")
            print("7. Set up Cargo and rustup paths")
            print("8. Configure clippy and rustfmt")
        
        print(f"\n{Colors.CYAN}Detailed instructions available in: jetbrains-setup.md{Colors.END}")

    def setup_visual_studio(self):
        """Setup Visual Studio configuration"""
        print(f"\n{Colors.GREEN}Setting up Visual Studio with Docker integration...{Colors.END}")
        
        print(f"{Colors.CYAN}Visual Studio Setup Instructions:{Colors.END}")
        print("1. Install 'Container Development Tools' workload")
        print("2. Install Docker Desktop for Windows")
        print("3. Add .devcontainer folder to your project")
        print("4. Use 'Open Folder in Container' feature")
        print("5. Configure CMake settings for C++ projects")
        
        print(f"\n{Colors.YELLOW}Visual Studio-specific notes:{Colors.END}")
        print("• Enable WSL2 integration in Docker Desktop")
        print("• Use 'Remote - Containers' extension if available")
        print("• Configure debugging for containerized applications")

    def setup_eclipse(self):
        """Setup Eclipse IDE configuration"""
        print(f"\n{Colors.GREEN}Setting up Eclipse with Docker integration...{Colors.END}")
        
        print(f"{Colors.CYAN}Eclipse Setup Instructions:{Colors.END}")
        print("1. Install Docker Tooling from Eclipse Marketplace")
        print("2. Install Remote Development Tools (if available)")
        print("3. Build container: docker build -t universal-claude-container .")
        print("4. Run container with workspace mounted")
        print("5. Configure remote projects and build tools")
        
        print(f"\n{Colors.YELLOW}Eclipse-specific tips:{Colors.END}")
        print("• Use Docker perspective for container management")
        print("• Configure remote launch configurations")
        print("• Set up Maven/Gradle for containerized builds")

    def setup_terminal_based(self, ide_type: str):
        """Setup terminal-based editors"""
        editor_names = {
            'neovim': 'Neovim',
            'emacs': 'Emacs'
        }
        
        editor_name = editor_names.get(ide_type, 'Terminal Editor')
        print(f"\n{Colors.GREEN}Setting up {editor_name} with container development...{Colors.END}")
        
        print(f"{Colors.CYAN}{editor_name} Setup Instructions:{Colors.END}")
        print("1. Build the container: docker build -t universal-claude-container .")
        print("2. Run container interactively:")
        print("   docker run -it --rm -v $(pwd):/workspace universal-claude-container")
        print("3. Use your editor inside the container environment")
        print("4. Install language servers and plugins in container")
        
        if ide_type == 'neovim':
            print(f"\n{Colors.YELLOW}Neovim-specific setup:{Colors.END}")
            print("• Configure LSP servers for all languages")
            print("• Install plugins: nvim-lspconfig, telescope, treesitter")
            print("• Set up debugging with nvim-dap")
        
        elif ide_type == 'emacs':
            print(f"\n{Colors.YELLOW}Emacs-specific setup:{Colors.END}")
            print("• Install language modes for all languages")
            print("• Configure company-mode for completions")
            print("• Set up projectile for project management")

    def setup_lightweight_editors(self, ide_type: str):
        """Setup lightweight editors"""
        editor_names = {
            'sublime': 'Sublime Text',
            'atom': 'Atom'
        }
        
        editor_name = editor_names.get(ide_type, 'Editor')
        print(f"\n{Colors.GREEN}Setting up {editor_name} with container development...{Colors.END}")
        
        print(f"{Colors.CYAN}{editor_name} Setup Instructions:{Colors.END}")
        print("1. Install Docker/container-related packages")
        print("2. Build container: docker build -t universal-claude-container .")
        print("3. Use integrated terminal to run container commands")
        print("4. Configure build systems for containerized development")
        
        if ide_type == 'sublime':
            print(f"\n{Colors.YELLOW}Sublime Text packages to install:{Colors.END}")
            print("• Docker")
            print("• LSP (Language Server Protocol)")
            print("• Terminus (integrated terminal)")
            print("• GitGutter")
        
        elif ide_type == 'atom':
            print(f"\n{Colors.YELLOW}Atom packages to install:{Colors.END}")
            print("• docker")
            print("• atom-ide-ui")
            print("• platformio-ide-terminal")
            print("• git-plus")

    def select_mcp_servers(self) -> List[str]:
        """Let user select which MCP servers to set up"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}MCP Server Selection{Colors.END}")
        print(f"{Colors.WHITE}Choose which MCP servers you want to set up for Claude Code integration.{Colors.END}")
        print(f"{Colors.YELLOW}You can always add more servers later by running this script again.{Colors.END}\n")
        
        selected_servers = []
        
        for i, (server_id, server_info) in enumerate(self.mcp_servers.items(), 1):
            print(f"{Colors.BOLD}{i}. {server_info['name']}{Colors.END}")
            print(f"   {Colors.CYAN}{server_info['description']}{Colors.END}")
            
            # Show requirements
            if server_info.get('env_vars'):
                print(f"   {Colors.YELLOW}Requires: {', '.join(server_info['env_vars'])}{Colors.END}")
            if server_info.get('setup_url'):
                print(f"   {Colors.BLUE}Setup URL: {server_info['setup_url']}{Colors.END}")
            
            if self.ask_yes_no(f"   Set up {server_info['name']}?", default=True):
                selected_servers.append(server_id)
                self.print_success(f"Added {server_info['name']} to setup list")
            else:
                print(f"   {Colors.YELLOW}Skipped {server_info['name']}{Colors.END}")
            
            print()  # Add spacing between servers
        
        if not selected_servers:
            self.print_warning("No MCP servers selected. You can set them up later.")
        else:
            print(f"{Colors.GREEN}Selected MCP servers: {', '.join([self.mcp_servers[s]['name'] for s in selected_servers])}{Colors.END}")
        
        return selected_servers

    def collect_api_keys(self, selected_servers: List[str]) -> Dict[str, str]:
        """Collect API keys from user for selected servers"""
        self.print_step(3, "API Keys Configuration", "Configure API keys for selected MCP servers")
        
        if not selected_servers:
            print(f"{Colors.YELLOW}No MCP servers selected, skipping API key collection.{Colors.END}")
            return {}
        
        keys = {}
        required_keys = set()
        
        # Collect all required keys for selected servers
        for server_id in selected_servers:
            server_info = self.mcp_servers[server_id]
            required_keys.update(server_info.get('env_vars', []))
        
        if not required_keys:
            print(f"{Colors.GREEN}Selected servers don't require API keys!{Colors.END}")
            return {}
        
        print(f"{Colors.CYAN}Collecting API keys for your selected MCP servers...{Colors.END}")
        print(f"{Colors.YELLOW}You can skip any key and set it up later.{Colors.END}\n")
        
        key_counter = 1
        
        # GitHub Personal Access Token
        if 'GITHUB_PERSONAL_ACCESS_TOKEN' in required_keys:
            print(f"{Colors.BOLD}{key_counter}. GitHub Personal Access Token{Colors.END}")
            print("   Used for: Repository management, issues, pull requests")
            print("   Required scopes: repo, read:org, read:user, gist, workflow")
            
            if self.ask_yes_no("   Do you want to set up GitHub integration now?"):
                print(f"   {Colors.CYAN}Opening GitHub token creation page...{Colors.END}")
                webbrowser.open('https://github.com/settings/tokens/new')
                self.wait_for_user("   Create your token and press Enter when ready...")
                
                while True:
                    token = input("   Enter your GitHub Personal Access Token: ").strip()
                    if token.startswith('ghp_') and len(token) > 20:
                        keys['GITHUB_PERSONAL_ACCESS_TOKEN'] = token
                        self.print_success("GitHub token saved!")
                        break
                    elif not token:
                        print("   Skipping GitHub integration (you can add this later)")
                        break
                    else:
                        print("   Invalid token format. GitHub tokens start with 'ghp_'")
            print()
            key_counter += 1
        
        # Composio API Key (for Notion, Figma, Zapier)
        if 'COMPOSIO_API_KEY' in required_keys:
            composio_servers = [s for s in selected_servers if s in ['notion', 'figma', 'zapier']]
            composio_names = [self.mcp_servers[s]['name'] for s in composio_servers]
            
            print(f"{Colors.BOLD}{key_counter}. Composio API Key{Colors.END}")
            print(f"   Used for: {', '.join(composio_names)} integrations")
            print("   Sign up at: https://app.composio.dev")
            
            if self.ask_yes_no("   Do you want to set up Composio integrations now?"):
                print(f"   {Colors.CYAN}Opening Composio dashboard...{Colors.END}")
                webbrowser.open('https://app.composio.dev')
                self.wait_for_user("   Create your account and get API key, then press Enter...")
                
                token = input("   Enter your Composio API Key (or press Enter to skip): ").strip()
                if token:
                    keys['COMPOSIO_API_KEY'] = token
                    self.print_success("Composio API key saved!")
                else:
                    print("   Skipping Composio integration (you can add this later)")
            print()
            key_counter += 1
        
        # PostgreSQL Connection String
        if 'POSTGRES_CONNECTION_STRING' in required_keys:
            print(f"{Colors.BOLD}{key_counter}. PostgreSQL Connection{Colors.END}")
            print("   Used for: Direct database interactions")
            print("   Format: postgresql://username:password@host:port/database")
            
            if self.ask_yes_no("   Do you have a PostgreSQL database to connect?"):
                while True:
                    conn_str = input("   Enter PostgreSQL connection string: ").strip()
                    if conn_str.startswith('postgresql://') or conn_str.startswith('postgres://'):
                        keys['POSTGRES_CONNECTION_STRING'] = conn_str
                        self.print_success("PostgreSQL connection saved!")
                        break
                    elif not conn_str:
                        print("   Skipping PostgreSQL connection (you can add this later)")
                        break
                    else:
                        print("   Invalid format. Use: postgresql://user:password@host:port/database")
            print()
            key_counter += 1
        
        # Upstash/Context7 Vector Database
        if 'UPSTASH_VECTOR_REST_URL' in required_keys:
            print(f"{Colors.BOLD}{key_counter}. Upstash Vector Database{Colors.END}")
            print("   Used for: Context7 semantic search and vector operations")
            print("   Create at: https://console.upstash.com")
            
            if self.ask_yes_no("   Do you want to set up Upstash Vector database now?"):
                print(f"   {Colors.CYAN}Opening Upstash console...{Colors.END}")
                webbrowser.open('https://console.upstash.com')
                self.wait_for_user("   Create your Vector database and get credentials, then press Enter...")
                
                print("   You'll need both the REST URL and REST Token from your Vector database")
                url = input("   Enter UPSTASH_VECTOR_REST_URL: ").strip()
                if url:
                    token = input("   Enter UPSTASH_VECTOR_REST_TOKEN: ").strip()
                    if token:
                        keys['UPSTASH_VECTOR_REST_URL'] = url
                        keys['UPSTASH_VECTOR_REST_TOKEN'] = token
                        self.print_success("Upstash Vector credentials saved!")
                    else:
                        print("   Skipping Context7 integration (missing token)")
                else:
                    print("   Skipping Context7 integration (missing URL)")
            print()
            key_counter += 1
        
        # Apidog API Key
        if 'APIDOG_API_KEY' in required_keys:
            print(f"{Colors.BOLD}{key_counter}. Apidog API Key{Colors.END}")
            print("   Used for: API documentation and testing")
            print("   Sign up at: https://apidog.com")
            
            if self.ask_yes_no("   Do you want to set up Apidog integration now?"):
                print(f"   {Colors.CYAN}Opening Apidog website...{Colors.END}")
                webbrowser.open('https://apidog.com')
                self.wait_for_user("   Create your account and get API key, then press Enter...")
                
                token = input("   Enter your Apidog API Key (or press Enter to skip): ").strip()
                if token:
                    keys['APIDOG_API_KEY'] = token
                    self.print_success("Apidog API key saved!")
                else:
                    print("   Skipping Apidog integration (you can add this later)")
            print()
            key_counter += 1
        
        if keys:
            print(f"{Colors.GREEN}API keys collected for: {', '.join(keys.keys())}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}No API keys collected. You can add them later by editing the Claude config.{Colors.END}")
        
        return keys

    def create_claude_config(self, selected_servers: List[str], api_keys: Dict[str, str]):
        """Create Claude Desktop configuration"""
        self.print_step(4, "Claude Desktop Configuration", "Setting up MCP servers for Claude Desktop")
        
        if not selected_servers:
            print(f"{Colors.YELLOW}No MCP servers selected. Skipping Claude Desktop configuration.{Colors.END}")
            print(f"{Colors.CYAN}You can run this script again later to add MCP servers.{Colors.END}")
            return
        
        # Ensure config directory exists
        self.claude_config_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Build MCP servers configuration
        mcp_config = {}
        
        for server_id in selected_servers:
            server_info = self.mcp_servers[server_id]
            
            # Check if we have required API keys
            missing_keys = [key for key in server_info.get('env_vars', []) if key not in api_keys]
            
            if missing_keys and server_id not in ['filesystem', 'sequential-thinking', 'puppeteer', 'memory']:
                print(f"   {Colors.YELLOW}Configuring {server_info['name']} without API keys (you can add them later){Colors.END}")
            
            # Build server configuration
            server_config = {
                'command': server_info['command'],
                'args': server_info['args'].copy()
            }
            
            # Handle special cases
            if server_id == 'filesystem':
                # Use local filesystem server if available
                fs_server_path = self.script_dir / '.devcontainer' / 'mcp-servers' / 'src' / 'filesystem' / 'dist' / 'index.js'
                if fs_server_path.exists():
                    server_config['command'] = 'node'
                    server_config['args'] = [str(fs_server_path), str(Path.cwd())]
                else:
                    server_config['args'] = ['-y', '@modelcontextprotocol/server-filesystem', str(Path.cwd())]
            
            # Add environment variables
            if server_info.get('env_vars'):
                server_config['env'] = {}
                for env_var in server_info['env_vars']:
                    if env_var in api_keys:
                        server_config['env'][env_var] = api_keys[env_var]
                    else:
                        # Add placeholder for missing keys
                        server_config['env'][env_var] = f"YOUR_{env_var}_HERE"
            
            # Add special environment variables
            if server_id == 'apidog':
                if 'APIDOG_API_KEY' in api_keys:
                    server_config['env'] = {
                        'HTTP_BASE_URL': 'https://api.apidog.com',
                        'HTTP_HEADERS': f'{{"Authorization": "Bearer {api_keys["APIDOG_API_KEY"]}", "Content-Type": "application/json"}}',
                        'HTTP_TIMEOUT': '30000'
                    }
                else:
                    server_config['env'] = {
                        'HTTP_BASE_URL': 'https://api.apidog.com',
                        'HTTP_HEADERS': '{"Authorization": "Bearer YOUR_APIDOG_API_KEY_HERE", "Content-Type": "application/json"}',
                        'HTTP_TIMEOUT': '30000'
                    }
            
            mcp_config[server_id] = server_config
            self.print_success(f"Configured {server_info['name']} MCP server")
        
        # Create complete configuration
        claude_config = {
            'mcpServers': mcp_config,
            'alwaysAllowReadOnly': True
        }
        
        # Write configuration file
        try:
            with open(self.claude_config_path, 'w') as f:
                json.dump(claude_config, f, indent=2)
            
            self.print_success(f"Claude Desktop configuration saved to: {self.claude_config_path}")
            
            # Show which servers need API keys
            servers_needing_keys = []
            for server_id in selected_servers:
                server_info = self.mcp_servers[server_id]
                missing_keys = [key for key in server_info.get('env_vars', []) if key not in api_keys]
                if missing_keys:
                    servers_needing_keys.append(f"{server_info['name']} ({', '.join(missing_keys)})")
            
            if servers_needing_keys:
                print(f"\n{Colors.YELLOW}Servers that still need API keys:{Colors.END}")
                for server in servers_needing_keys:
                    print(f"  • {server}")
                print(f"{Colors.CYAN}Edit {self.claude_config_path} to add your API keys later.{Colors.END}")
            
            print(f"\n{Colors.YELLOW}Important: Restart Claude Desktop for changes to take effect!{Colors.END}")
            
        except Exception as e:
            self.print_error(f"Failed to write Claude config: {e}")
            print(f"{Colors.CYAN}Manual setup required. Copy this configuration to {self.claude_config_path}:{Colors.END}")
            print(json.dumps(claude_config, indent=2))

    def install_mcp_servers(self, selected_servers: List[str]):
        """Install MCP servers globally"""
        self.print_step(5, "Installing MCP Servers", "Installing global MCP server packages")
        
        if not selected_servers:
            print(f"{Colors.YELLOW}No MCP servers selected for installation.{Colors.END}")
            return
        
        # Map servers to their npm packages
        server_packages = {
            'github': '@modelcontextprotocol/server-github',
            'sequential-thinking': '@modelcontextprotocol/server-sequential-thinking', 
            'postgres': '@modelcontextprotocol/server-postgres',
            'puppeteer': 'puppeteer-mcp-server',
            'memory': '@modelcontextprotocol/server-memory',
            'context7': '@upstash/context7',
            'notion': '@composio/mcp',
            'figma': '@composio/mcp',
            'zapier': '@composio/mcp',
            'apidog': '@modelcontextprotocol/server-http'
        }
        
        # Get unique packages to install
        packages_to_install = set()
        for server_id in selected_servers:
            if server_id in server_packages:
                packages_to_install.add(server_packages[server_id])
            elif server_id == 'filesystem':
                # Filesystem server is built locally
                continue
        
        if not packages_to_install:
            print(f"{Colors.GREEN}Selected servers don't require npm package installation!{Colors.END}")
            return
        
        print(f"{Colors.CYAN}Installing packages for selected MCP servers...{Colors.END}")
        
        for package in packages_to_install:
            print(f"Installing {package}...")
            try:
                result = subprocess.run(['npm', 'install', '-g', package], 
                                      capture_output=True, text=True, timeout=120)
                if result.returncode == 0:
                    self.print_success(f"Installed {package}")
                else:
                    self.print_warning(f"Could not install {package}: {result.stderr.strip()}")
            except subprocess.TimeoutExpired:
                self.print_warning(f"Timeout installing {package}")
            except Exception as e:
                self.print_warning(f"Error installing {package}: {e}")
        
        # Set up Composio integrations if selected
        composio_servers = [s for s in selected_servers if s in ['notion', 'figma', 'zapier']]
        if composio_servers and '@composio/mcp' in packages_to_install:
            print(f"\n{Colors.CYAN}Setting up Composio integrations...{Colors.END}")
            for server in composio_servers:
                try:
                    print(f"Setting up {self.mcp_servers[server]['name']}...")
                    result = subprocess.run(['npx', '@composio/mcp@latest', 'setup', server, '--client', 'claude'], 
                                          capture_output=True, text=True, timeout=60)
                    if result.returncode == 0:
                        self.print_success(f"Set up {self.mcp_servers[server]['name']} integration")
                    else:
                        self.print_warning(f"Could not set up {server}: {result.stderr.strip()}")
                except Exception as e:
                    self.print_warning(f"Error setting up {server}: {e}")

    def setup_container(self, ide_type: str):
        """Setup the container based on IDE choice"""
        self.print_step(6, "Container Setup", "Preparing the development container")
        
        print(f"{Colors.CYAN}Container setup for {ide_type}...{Colors.END}")
        
        if ide_type == 'vscode':
            print("VS Code will automatically build the container when you open the project.")
            print("Make sure the .devcontainer folder is in your project root.")
        else:
            print("Building the container manually...")
            if self.ask_yes_no("Would you like to build the container now?"):
                self.build_container()
        
        self.create_project_template()

    def build_container(self):
        """Build the Docker container"""
        print(f"\n{Colors.CYAN}Building Universal Claude Code Container...{Colors.END}")
        print("This may take 10-15 minutes the first time...")
        
        dockerfile_path = self.script_dir / '.devcontainer' / 'Dockerfile'
        if not dockerfile_path.exists():
            dockerfile_path = self.script_dir / '.devcontainer' / 'Dockerfile.universal'
        
        try:
            # Build the container
            cmd = ['docker', 'build', '-t', 'universal-claude-container', '-f', str(dockerfile_path), str(self.script_dir)]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            
            # Show progress
            for line in process.stdout:
                print(f"   {line.strip()}")
            
            process.wait()
            
            if process.returncode == 0:
                self.print_success("Container built successfully!")
            else:
                self.print_error("Container build failed!")
                
        except Exception as e:
            self.print_error(f"Error building container: {e}")

    def create_project_template(self):
        """Create a sample project structure"""
        print(f"\n{Colors.CYAN}Creating project template...{Colors.END}")
        
        template_dir = Path.cwd() / 'sample-project'
        template_dir.mkdir(exist_ok=True)
        
        # Copy devcontainer files
        devcontainer_src = self.script_dir / '.devcontainer'
        devcontainer_dst = template_dir / '.devcontainer'
        
        if devcontainer_src.exists():
            shutil.copytree(devcontainer_src, devcontainer_dst, dirs_exist_ok=True)
            
            # Rename universal files if needed
            universal_files = [
                ('Dockerfile.universal', 'Dockerfile'),
                ('devcontainer.universal.json', 'devcontainer.json'),
                ('post-create-universal.sh', 'post-create.sh')
            ]
            
            for old_name, new_name in universal_files:
                old_path = devcontainer_dst / old_name
                new_path = devcontainer_dst / new_name
                if old_path.exists() and not new_path.exists():
                    old_path.rename(new_path)
            
            self.print_success(f"Sample project created at: {template_dir}")
            print(f"   You can copy the .devcontainer folder to any project")

    def test_setup(self):
        """Test the setup"""
        self.print_step(7, "Testing Setup", "Verifying everything is working correctly")
        
        tests = [
            ("Docker", lambda: subprocess.run(['docker', '--version'], capture_output=True)),
            ("Node.js", lambda: subprocess.run(['node', '--version'], capture_output=True)),
            ("Claude Config", lambda: self.claude_config_path.exists())
        ]
        
        all_passed = True
        
        for test_name, test_func in tests:
            try:
                if callable(test_func):
                    result = test_func()
                    if hasattr(result, 'returncode'):
                        success = result.returncode == 0
                    else:
                        success = bool(result)
                else:
                    success = test_func
                
                if success:
                    self.print_success(f"{test_name} test passed")
                else:
                    self.print_error(f"{test_name} test failed")
                    all_passed = False
                    
            except Exception as e:
                self.print_error(f"{test_name} test failed: {e}")
                all_passed = False
        
        return all_passed

    def show_next_steps(self, ide_type: str):
        """Show next steps to the user"""
        self.print_step(8, "Setup Complete!", "Your Universal Claude Code Container is ready")
        
        print(f"{Colors.GREEN}{Colors.BOLD}🎉 Setup completed successfully!{Colors.END}\n")
        
        print(f"{Colors.CYAN}{Colors.BOLD}Next Steps:{Colors.END}")
        
        if ide_type == 'vscode':
            print("1. Open VS Code in your project directory")
            print("2. Copy the .devcontainer folder to your project root")
            print("3. Press Ctrl+Shift+P and select 'Dev Containers: Reopen in Container'")
            print("4. VS Code will build and start the container automatically")
        elif ide_type in ['android_studio', 'intellij', 'clion', 'pycharm', 'webstorm', 'rider', 'goland', 'rustrover']:
            print("1. Copy the .devcontainer folder to your project root")
            print("2. Install Docker plugin in your JetBrains IDE")
            print("3. Build the container: docker build -t my-project .")
            print("4. Configure remote toolchain to use the container")
            print("5. Set up project SDK/interpreter to use container environment")
        elif ide_type == 'visual_studio':
            print("1. Install 'Container Development Tools' workload")
            print("2. Copy the .devcontainer folder to your project root")
            print("3. Use 'Open Folder in Container' feature")
            print("4. Configure build and debugging for container")
        elif ide_type == 'eclipse':
            print("1. Install Docker Tooling from Eclipse Marketplace")
            print("2. Copy the .devcontainer folder to your project root")
            print("3. Build the container: docker build -t my-project .")
            print("4. Configure remote projects and launch configurations")
        elif ide_type in ['neovim', 'emacs']:
            print("1. Build the container: docker build -t my-project .")
            print("2. Run container: docker run -it --rm -v $(pwd):/workspace my-project")
            print("3. Use your editor inside the container environment")
            print("4. Configure language servers and plugins")
        elif ide_type in ['sublime', 'atom']:
            print("1. Install Docker/container packages in your editor")
            print("2. Build the container: docker build -t my-project .")
            print("3. Use integrated terminal for container commands")
            print("4. Configure build systems for containerized development")
        else:
            print("1. Copy the .devcontainer folder to your project root")
            print("2. Build the container: docker build -t my-project .")
            print("3. Run the container with your project mounted")
            print("4. Configure your IDE to use the container")
        
        print(f"\n{Colors.YELLOW}{Colors.BOLD}Important:{Colors.END}")
        print("• Restart Claude Desktop to load the new MCP servers")
        print("• Check Claude Desktop logs if servers don't connect")
        print("• API keys are stored in the Claude Desktop config")
        
        print(f"\n{Colors.CYAN}{Colors.BOLD}Your MCP Servers:{Colors.END}")
        if hasattr(self, '_selected_servers') and self._selected_servers:
            for server_id in self._selected_servers:
                server_info = self.mcp_servers[server_id]
                print(f"• {server_info['name']}: {server_info['description']}")
        else:
            print(f"{Colors.YELLOW}No MCP servers were configured in this session.{Colors.END}")
            print(f"{Colors.CYAN}Run this script again to add MCP servers.{Colors.END}")
        
        print(f"\n{Colors.MAGENTA}{Colors.BOLD}Quick Commands:{Colors.END}")
        print("• new-react <name>     - Create React app")
        print("• new-flutter <name>   - Create Flutter app")
        print("• android-emulator     - Start Android emulator")
        print("• py-env               - Create Python environment")
        print("• test-all             - Run all project tests")
        
        print(f"\n{Colors.GREEN}Happy coding with Claude Code! 🚀{Colors.END}")

    def run_setup(self):
        """Run the complete setup process"""
        try:
            self.print_banner()
            
            # Step 1: Check prerequisites
            if not self.check_prerequisites():
                return False
            
            self.wait_for_user()
            
            # Step 2: Select IDE
            ide_type = self.select_ide()
            
            self.wait_for_user()
            
            # Step 2.5: Select MCP servers
            selected_servers = self.select_mcp_servers()
            
            self.wait_for_user()
            
            # Step 3: Collect API keys
            api_keys = self.collect_api_keys(selected_servers)
            
            self.wait_for_user()
            
            # Step 4: Create Claude configuration
            self.create_claude_config(selected_servers, api_keys)
            
            self.wait_for_user()
            
            # Step 5: Install MCP servers
            self.install_mcp_servers(selected_servers)
            
            self.wait_for_user()
            
            # Step 6: Setup container
            self.setup_container(ide_type)
            
            # IDE-specific setup
            if ide_type == 'vscode':
                self.setup_vscode()
            elif ide_type in ['android_studio', 'intellij', 'clion', 'pycharm', 'webstorm', 'rider', 'goland', 'rustrover']:
                self.setup_jetbrains(ide_type)
            elif ide_type == 'visual_studio':
                self.setup_visual_studio()
            elif ide_type == 'eclipse':
                self.setup_eclipse()
            elif ide_type in ['neovim', 'emacs']:
                self.setup_terminal_based(ide_type)
            elif ide_type in ['sublime', 'atom']:
                self.setup_lightweight_editors(ide_type)
            else:
                print(f"\n{Colors.YELLOW}Manual setup required for your IDE.{Colors.END}")
                print("Please refer to the documentation for container integration.")
            
            self.wait_for_user()
            
            # Step 7: Test setup
            test_passed = self.test_setup()
            
            self.wait_for_user()
            
            # Step 8: Show next steps
            self._selected_servers = selected_servers  # Store for final summary
            self.show_next_steps(ide_type)
            
            return test_passed
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}Setup interrupted by user.{Colors.END}")
            return False
        except Exception as e:
            print(f"\n\n{Colors.RED}Setup failed with error: {e}{Colors.END}")
            return False

def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print("""
Universal Claude Code Container Setup

This script guides you through setting up the complete development environment
for Claude Code with support for any project type.

Usage:
    python setup.py        Run interactive setup
    python setup.py --help Show this help message

Features:
• Multi-language support (JavaScript, Python, Go, Rust, Java, C++, etc.)
• Mobile development (Flutter, React Native, Android SDK)
• 10 MCP servers for enhanced Claude Code capabilities
• IDE integration (VS Code, JetBrains IDEs)
• Automatic container configuration and deployment

Requirements:
• Docker
• Node.js and npm
• Git
• Your preferred IDE

The setup process will:
1. Check prerequisites
2. Configure your IDE
3. Collect API keys for MCP servers
4. Set up Claude Desktop configuration
5. Install and configure MCP servers
6. Build and test the container
7. Provide next steps and usage instructions
        """)
        return
    
    setup = UniversalContainerSetup()
    success = setup.run_setup()
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()