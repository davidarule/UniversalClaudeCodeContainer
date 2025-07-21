#!/bin/bash
set -e

echo "🚀 Setting up Universal Claude Code Development Environment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Create necessary directories
echo -e "${BLUE}📁 Creating development directories...${NC}"
mkdir -p ~/.cache ~/.config ~/.local/share ~/.ssh ~/.gnupg
mkdir -p ~/.android ~/.gradle ~/.m2 ~/.cargo ~/.rustup ~/.go
mkdir -p ~/projects ~/tools ~/scripts

# Set proper permissions
chmod 700 ~/.ssh ~/.gnupg 2>/dev/null || true

# Configure Git if not already configured
echo -e "${BLUE}🔧 Configuring Git...${NC}"
if [ -z "$(git config --global user.name)" ]; then
    echo "Git user.name not set. Please configure:"
    echo "git config --global user.name 'Your Name'"
fi
if [ -z "$(git config --global user.email)" ]; then
    echo "Git user.email not set. Please configure:"
    echo "git config --global user.email 'your.email@example.com'"
fi

# Setup Android environment
echo -e "${BLUE}📱 Setting up Android development environment...${NC}"
if [ -d "/opt/android-sdk" ]; then
    # Create Android Virtual Device
    echo "no" | ${ANDROID_HOME}/cmdline-tools/latest/bin/avdmanager create avd \
        -n "Claude_Android_API_34" \
        -k "system-images;android-34;google_apis;x86_64" \
        -d "pixel_4" || echo "AVD may already exist"
    
    # Accept any additional licenses
    yes | ${ANDROID_HOME}/cmdline-tools/latest/bin/sdkmanager --licenses >/dev/null 2>&1 || true
fi

# Setup Flutter
echo -e "${BLUE}🦋 Configuring Flutter...${NC}"
if [ -d "/opt/flutter" ]; then
    flutter config --no-analytics
    flutter config --enable-web
    flutter config --enable-linux-desktop
    flutter config --android-sdk ${ANDROID_HOME}
    
    # Pre-download Flutter dependencies
    flutter precache --web --linux --android
    
    echo -e "${GREEN}✅ Flutter setup complete${NC}"
    flutter doctor -v
fi

# Setup Node.js and npm
echo -e "${BLUE}📦 Setting up Node.js environment...${NC}"
# Update npm to latest
npm install -g npm@latest

# Setup Python environment
echo -e "${BLUE}🐍 Setting up Python environment...${NC}"
# Create a default virtual environment
python3 -m venv ~/.venv/default
echo "Default Python virtual environment created at ~/.venv/default"

# Setup Rust environment
echo -e "${BLUE}🦀 Setting up Rust environment...${NC}"
if command -v rustc >/dev/null 2>&1; then
    rustup default stable
    rustup component add clippy rustfmt rust-analyzer
fi

# Setup Go environment
echo -e "${BLUE}🐹 Setting up Go environment...${NC}"
if command -v go >/dev/null 2>&1; then
    # Set up Go module proxy
    go env -w GOPROXY=https://proxy.golang.org,direct
    go env -w GOSUMDB=sum.golang.org
fi

# Setup Java environment
echo -e "${BLUE}☕ Setting up Java environment...${NC}"
if command -v java >/dev/null 2>&1; then
    # Set up JAVA_HOME in profile
    echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.zshrc
fi

# Install additional MCP servers
echo -e "${BLUE}🔌 Installing MCP servers...${NC}"

# Install all MCP servers
npm install -g @modelcontextprotocol/server-github >/dev/null 2>&1 || echo "GitHub MCP server already installed"
npm install -g @modelcontextprotocol/server-sequential-thinking >/dev/null 2>&1 || echo "Sequential Thinking MCP server already installed"
npm install -g @modelcontextprotocol/server-postgres >/dev/null 2>&1 || echo "PostgreSQL MCP server already installed"
npm install -g puppeteer-mcp-server >/dev/null 2>&1 || echo "Puppeteer MCP server already installed"
npm install -g @modelcontextprotocol/server-memory >/dev/null 2>&1 || echo "Memory MCP server already installed"

# Install Composio MCP for external integrations
npm install -g @composio/mcp >/dev/null 2>&1 || echo "Composio MCP already installed"

# Setup development shortcuts
echo -e "${BLUE}⚡ Creating development shortcuts...${NC}"
cat > ~/scripts/dev-shortcuts.sh << 'EOF'
#!/bin/bash
# Development shortcuts for Claude Code container

# Quick project setup
new-react() { npx create-react-app "$1" && cd "$1"; }
new-next() { npx create-next-app "$1" && cd "$1"; }
new-vue() { npm create vue@latest "$1" && cd "$1"; }
new-angular() { ng new "$1" && cd "$1"; }
new-flutter() { flutter create "$1" && cd "$1"; }
new-expo() { npx create-expo-app "$1" && cd "$1"; }
new-ionic() { ionic start "$1" && cd "$1"; }

# Mobile development
android-emulator() { 
    ${ANDROID_HOME}/emulator/emulator -avd Claude_Android_API_34 -no-audio -no-window &
}

# Docker shortcuts
docker-clean() { 
    docker system prune -f
    docker volume prune -f
}

# Git shortcuts
git-setup() {
    git init
    git add .
    git commit -m "Initial commit"
}

# Python shortcuts
py-env() {
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
}

# Claude Code shortcuts
claude-help() {
    echo "Claude Code Commands:"
    echo "• claude auth login     - Authenticate with Claude"
    echo "• claude chat          - Start interactive chat"
    echo "• claude ask 'question' - Ask Claude a question"
    echo "• claude review        - Review current changes"
    echo "• claude docs          - Generate documentation"
    echo "• claude test          - Generate tests"
    echo "• claude explain       - Explain code"
    echo "• claude --help        - Full command reference"
}

claude-setup() {
    echo "Setting up Claude Code for this project..."
    claude auth login
    echo "Claude Code is ready to use!"
}

# Testing shortcuts
test-all() {
    echo "Running all tests..."
    # Node.js projects
    if [ -f "package.json" ]; then
        npm test 2>/dev/null || echo "No npm tests"
    fi
    # Python projects
    if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
        python -m pytest 2>/dev/null || echo "No Python tests"
    fi
    # Flutter projects
    if [ -f "pubspec.yaml" ]; then
        flutter test 2>/dev/null || echo "No Flutter tests"
    fi
}
EOF

chmod +x ~/scripts/dev-shortcuts.sh
echo "source ~/scripts/dev-shortcuts.sh" >> ~/.zshrc

# Setup VS Code settings
echo -e "${BLUE}⚙️  Setting up VS Code workspace...${NC}"
mkdir -p ~/.vscode-server/data/Machine
cat > ~/.vscode-server/data/Machine/settings.json << 'EOF'
{
    "workbench.colorTheme": "GitHub Dark",
    "workbench.iconTheme": "material-icon-theme",
    "editor.fontFamily": "'Fira Code', 'Cascadia Code', Consolas, 'Courier New', monospace",
    "editor.fontLigatures": true,
    "editor.fontSize": 14,
    "editor.lineHeight": 1.5,
    "editor.minimap.enabled": false,
    "editor.rulers": [80, 120],
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "terminal.integrated.fontSize": 13,
    "workbench.startupEditor": "welcomePage"
}
EOF

# Create sample project structure
echo -e "${BLUE}📝 Creating sample project templates...${NC}"
mkdir -p ~/templates/{web,mobile,backend,ml,devops}

# Web template
cat > ~/templates/web/README.md << 'EOF'
# Web Development Template

This template includes:
- React/Next.js for frontend
- Node.js/Express for backend
- TypeScript configuration
- ESLint and Prettier setup
- Testing with Jest
- Docker configuration

## Quick Start
```bash
# Frontend
npx create-next-app@latest my-app --typescript --tailwind --app

# Backend
mkdir my-api && cd my-api
npm init -y
npm install express cors helmet morgan
npm install -D nodemon @types/node typescript
```
EOF

# Mobile template
cat > ~/templates/mobile/README.md << 'EOF'
# Mobile Development Template

This template includes:
- Flutter for cross-platform apps
- React Native with Expo
- Ionic with Angular/React
- Android native development

## Quick Start
```bash
# Flutter
flutter create my_app

# React Native with Expo
npx create-expo-app MyApp

# Ionic
ionic start MyApp tabs --type=angular
```
EOF

# Setup Claude Code CLI
echo -e "${BLUE}🤖 Setting up Claude Code CLI...${NC}"
if command -v claude >/dev/null 2>&1; then
    # Claude Code is installed, set up configuration
    echo "Claude Code CLI is available!"
    echo "Run 'claude auth login' to authenticate with your account"
    echo "Run 'claude --help' to see available commands"
else
    echo "Installing Claude Code CLI..."
    curl -fsSL https://claude.ai/cli/install.sh | bash
    source ~/.bashrc || source ~/.zshrc || true
fi

# Display environment info
echo -e "\n${GREEN}🎉 Universal Claude Code Development Environment Setup Complete!${NC}\n"

echo -e "${YELLOW}📋 Environment Summary:${NC}"
echo "=================================="
echo "🐧 OS: $(lsb_release -d | cut -f2)"
echo "🔧 Node.js: $(node --version 2>/dev/null || echo 'Not available')"
echo "🐍 Python: $(python3 --version 2>/dev/null || echo 'Not available')"
echo "☕ Java: $(java --version 2>/dev/null | head -1 || echo 'Not available')"
echo "🦀 Rust: $(rustc --version 2>/dev/null || echo 'Not available')"
echo "🐹 Go: $(go version 2>/dev/null || echo 'Not available')"
echo "🦋 Flutter: $(flutter --version 2>/dev/null | head -1 || echo 'Not available')"
echo "📱 Android SDK: $([ -d "$ANDROID_HOME" ] && echo 'Installed' || echo 'Not available')"
echo "🐳 Docker: $(docker --version 2>/dev/null || echo 'Not available')"
echo "🔧 Git: $(git --version 2>/dev/null || echo 'Not available')"
echo "🤖 Claude Code: $(claude --version 2>/dev/null || echo 'Run setup to install')"

echo -e "\n${YELLOW}🚀 Available Commands:${NC}"
echo "=================================="
echo "• new-react <name>      - Create new React app"
echo "• new-next <name>       - Create new Next.js app"
echo "• new-flutter <name>    - Create new Flutter app"
echo "• new-expo <name>       - Create new Expo app"
echo "• android-emulator      - Start Android emulator"
echo "• py-env               - Create Python virtual environment"
echo "• test-all             - Run all tests in project"
echo "• docker-clean         - Clean Docker system"
echo "• claude-help          - Show Claude Code commands"
echo "• claude-setup         - Setup Claude Code authentication"

echo -e "\n${YELLOW}📁 Useful Directories:${NC}"
echo "=================================="
echo "• ~/projects/          - Your project workspace"
echo "• ~/templates/         - Project templates"
echo "• ~/scripts/           - Custom scripts"
echo "• ~/.venv/default/     - Default Python environment"

echo -e "\n${BLUE}💡 Next Steps:${NC}"
echo "1. Configure Git: git config --global user.name 'Your Name'"
echo "2. Configure Git: git config --global user.email 'your.email@example.com'"
echo "3. Authenticate Claude Code: claude auth login"
echo "4. Start a new project in ~/projects/"
echo "5. Run 'source ~/.zshrc' to load all shortcuts"

echo -e "\n${GREEN}Happy coding with Claude Code! 🚀${NC}\n"