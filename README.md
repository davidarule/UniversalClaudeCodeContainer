# Universal Claude Code Container

The perfect development container for Claude Code to work in any project type. Supports web, mobile (Android/iOS), backend, ML, and DevOps development with **11 MCP servers** for enhanced AI assistance.

## 🌟 Features

### Multi-Language Support
- **Web Development**: JavaScript/TypeScript, React, Vue, Angular, Next.js, Node.js
- **Mobile Development**: Flutter, React Native, Ionic, Cordova, Android SDK
- **Backend Development**: Python, Java, Go, Rust, PHP, .NET, Ruby, C/C++
- **Database Support**: PostgreSQL, MySQL, SQLite, MongoDB, Redis
- **DevOps**: Docker, Kubernetes, Terraform, Cloud CLIs (AWS, Azure, GCP)

### Pre-installed Tools
- **Build Tools**: CMake, Ninja, Maven, Gradle, Cargo, Go modules
- **Code Quality**: ESLint, Prettier, Black, Clippy, Rustfmt, Clang-format
- **Testing**: Jest, Pytest, JUnit, Flutter Test, Cypress, Playwright
- **Version Control**: Git, Git LFS, GitHub CLI
- **AI Assistant**: Claude Code CLI for AI-powered development
- **Editors**: Vim, Neovim, Nano (VS Code is the primary IDE)

### Mobile Development
- **Android SDK**: API levels 32-34, build tools, emulator, system images
- **Flutter**: Stable channel with web and desktop support
- **React Native**: CLI, Expo CLI, EAS CLI
- **Ionic**: CLI with Capacitor support
- **Appium**: For mobile testing automation

### MCP Servers (11 Total)
1. **GitHub** - Repository management, issues, PRs, releases
2. **File System** - Advanced file operations beyond standard Claude Code access
3. **Sequential Thinking** - Enhanced reasoning and problem-solving capabilities
4. **Puppeteer** - Web automation, scraping, and browser control
5. **PostgreSQL** - Direct database interactions and queries
6. **Memory Bank** - Persistent context and memory across sessions
7. **Context7** - Vector database for semantic search and contextual retrieval
8. **Notion** - Workspace integration and documentation sync (via Composio)
9. **Figma** - Design tool integration and asset management (via Composio)
10. **Zapier** - Cross-app automation and workflow integration (via Composio)
11. **Apidog** - API documentation, testing, and client generation

## 🚀 Quick Start

### Option 1: Interactive Setup (Recommended)
```bash
# Clone the repository
git clone https://github.com/davidarule/UniversalClaudeCodeContainer.git
cd UniversalClaudeCodeContainer

# Run the interactive setup script
python3 setup.py
```

The setup script will guide you through:
1. Prerequisites check (Docker, Node.js, Git)
2. IDE selection (16 supported IDEs)
3. MCP server selection (choose any/all of 11 servers)
4. API key collection (only for selected servers)
5. Claude Desktop configuration
6. Container setup and testing

### Option 2: Manual Setup
1. Copy the `.devcontainer/` folder to your project root
2. Rename files:
   - `Dockerfile.universal` → `Dockerfile`
   - `devcontainer.universal.json` → `devcontainer.json`
   - `post-create-universal.sh` → `post-create.sh`
3. Open project in your IDE and select "Reopen in Container"

## 🎯 Supported IDEs (16 Total)

### **Microsoft IDEs**
- **VS Code** (Recommended - Full container support)
- **Visual Studio** (Windows C++/.NET projects)

### **JetBrains Family**
- **Android Studio** (Mobile development)
- **IntelliJ IDEA** (Java/Kotlin/Scala)
- **CLion** (C/C++ projects)
- **PyCharm** (Python development)
- **WebStorm** (Web development)
- **Rider** (C#/.NET development)
- **GoLand** (Go development)
- **RustRover** (Rust development)

### **Other Popular IDEs**
- **Eclipse** (Java/C++ development)
- **Neovim/Vim** (Terminal-based with LSP)
- **Emacs** (Terminal/GUI-based)
- **Sublime Text** (Lightweight editor)
- **Atom** (GitHub's editor)
- **Other** (Manual setup option)

## 📁 Project Structure

```
UniversalClaudeCodeContainer/
├── README.md                              # This file
├── setup.py                               # Interactive setup script
├── .devcontainer/
│   ├── Dockerfile.universal               # Universal container definition
│   ├── devcontainer.universal.json       # VS Code container config
│   ├── post-create-universal.sh          # Container setup script
│   ├── README-Universal.md               # Detailed documentation
│   └── jetbrains-setup.md                # JetBrains IDE instructions
├── .github/
│   ├── claude_desktop_config_example.json # Complete MCP config
│   ├── mcp-all-servers-setup.md          # Comprehensive MCP guide
│   ├── mcp-github-setup.md               # GitHub MCP setup
│   ├── mcp-apidog-setup.md               # Apidog MCP setup
│   └── mcp-filesystem-setup.md           # File System MCP setup
└── examples/                             # Example project templates
```

## 🔧 Configuration

### MCP Servers Setup
Copy `.github/claude_desktop_config_example.json` to your Claude Desktop config location:
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/claude/claude_desktop_config.json`

Replace placeholder API keys with your actual keys:
- GitHub Personal Access Token
- Composio API Key (for Notion, Figma, Zapier)
- Apidog API Key
- PostgreSQL connection string
- Upstash Vector credentials (for Context7)

### Environment Variables
The container sets up:
```bash
ANDROID_HOME=/opt/android-sdk
FLUTTER_HOME=/opt/flutter
JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```

## 🛠️ Available Commands

### Quick Project Creation
```bash
new-react <name>      # Create React app
new-next <name>       # Create Next.js app
new-vue <name>        # Create Vue app
new-angular <name>    # Create Angular app
new-flutter <name>    # Create Flutter app
new-expo <name>       # Create Expo app
new-ionic <name>      # Create Ionic app
```

### Development Tools
```bash
android-emulator      # Start Android emulator
py-env               # Create Python virtual environment
test-all             # Run all tests in project
docker-clean         # Clean Docker system
git-setup            # Initialize git repository
claude-help          # Show Claude Code commands
claude-setup         # Setup Claude Code authentication
```

### Claude Code Integration
```bash
claude auth login     # Authenticate with Claude
claude chat          # Start interactive chat
claude ask "question" # Ask Claude a question
claude review        # Review current changes
claude docs          # Generate documentation
claude test          # Generate tests
claude explain       # Explain code
```

## 📱 Mobile Development

### Android Setup
- SDK API levels 32, 33, 34 pre-installed
- Build tools and platform tools included
- Pre-configured AVD: "Claude_Android_API_34"
- Start emulator: `android-emulator`

### Flutter Development
- Stable channel with latest version
- Web and desktop support enabled
- Android SDK integration configured
- Pre-cached dependencies for faster builds

### React Native
- React Native CLI and Expo CLI installed
- EAS CLI for Expo Application Services
- Metro bundler and debugging tools

## 🌐 Web Development

### Frontend Frameworks
- React with Create React App
- Next.js for full-stack React
- Vue.js with Vue CLI
- Angular with Angular CLI
- Svelte and SvelteKit support

### Build Tools
- Webpack, Parcel, Vite
- TypeScript and Babel
- ESLint and Prettier
- PostCSS and Tailwind CSS

### Testing
- Jest for unit testing
- Cypress for e2e testing
- Playwright for browser testing
- Puppeteer for automation

## 🗄️ Database Support

### Included Clients
- PostgreSQL (`psql`)
- MySQL (`mysql`)
- SQLite (`sqlite3`)
- MongoDB (`mongosh`)
- Redis (`redis-cli`)

### GUI Tools (via VS Code extensions)
- PostgreSQL Explorer
- MongoDB for VS Code
- Redis Explorer
- SQLite Viewer

## ☁️ Cloud Development

### Cloud CLIs
- AWS CLI v2
- Azure CLI
- Google Cloud CLI
- Docker and Docker Compose

### Kubernetes
- kubectl
- Helm
- Minikube (for local clusters)

### Infrastructure as Code
- Terraform
- Docker Compose
- Kubernetes manifests

## 🔌 MCP Servers Details

### Core Development Servers
- **GitHub**: Complete repository management, issue tracking, PR automation
- **File System**: Advanced file operations, directory traversal, file watching
- **Sequential Thinking**: Enhanced reasoning for complex problem solving
- **Memory Bank**: Persistent context and preferences across sessions

### Database & Search
- **PostgreSQL**: Direct database queries, schema management, migrations
- **Context7**: Vector search, semantic similarity, AI-powered recommendations

### External Integrations
- **Puppeteer**: Web scraping, automation, screenshot generation
- **Notion**: Documentation sync, project management, knowledge base
- **Figma**: Design asset export, UI integration, design system sync
- **Zapier**: Workflow automation, cross-app integrations
- **Apidog**: API testing, documentation generation, client code creation

## 🎯 Use Cases

### Perfect for Claude Code
- **Any project type**: Web, mobile, backend, ML, DevOps
- **Cross-platform development**: Build for multiple platforms
- **API integrations**: Full MCP server suite for external services
- **Team collaboration**: Consistent environment across developers
- **Learning**: All tools available for exploration

### Project Types Supported
- **E-commerce sites** (React/Next.js + Node.js + PostgreSQL)
- **Mobile apps** (Flutter or React Native)
- **APIs and microservices** (Python/FastAPI, Node.js/Express, Go)
- **ML/AI projects** (Python with TensorFlow/PyTorch)
- **DevOps pipelines** (Docker, Kubernetes, Terraform)
- **Desktop applications** (Flutter desktop, Electron)

## 🔧 Customization

### Adding Languages
Edit `Dockerfile.universal` to add support for additional languages:
```dockerfile
# Add new language runtime
RUN apt-get install -y new-language-runtime

# Install language-specific tools
RUN language-package-manager install tools
```

### Adding VS Code Extensions
Edit `devcontainer.universal.json` extensions array:
```json
"extensions": [
    "existing.extensions",
    "new.extension.id"
]
```

### Adding MCP Servers
Edit `.github/claude_desktop_config_example.json`:
```json
"new-server": {
    "command": "npx",
    "args": ["-y", "new-mcp-server"],
    "env": {
        "API_KEY": "your-key"
    }
}
```

## 🐛 Troubleshooting

### Common Issues

**Container Build Fails**
```bash
# Clear Docker cache
docker system prune -a
# Rebuild container
docker build --no-cache -t universal-claude-container .
```

**MCP Servers Not Connecting**
- Restart Claude Desktop after config changes
- Check API keys are correct in config file
- Verify internet connection for server downloads
- Check Claude Desktop logs: Help → Show Logs

**Android Emulator Won't Start**
```bash
# Check KVM support (Linux)
ls -la /dev/kvm
# Enable hardware acceleration
android-emulator
```

**Flutter Doctor Issues**
```bash
flutter doctor -v
flutter config --android-sdk $ANDROID_HOME
```

### Performance Optimization
- Use volume mounts for persistent data
- Enable BuildKit for faster Docker builds
- Use ccache for C++ compilation
- Configure IDE for better performance

## 📚 Documentation

### Additional Resources
- [Detailed Container Documentation](.devcontainer/README-Universal.md)
- [JetBrains IDE Setup](jetbrains-setup.md)
- [MCP Servers Guide](.github/mcp-all-servers-setup.md)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/remote/containers)

### Sample Projects
Check the `examples/` directory for:
- Web development templates
- Mobile app templates
- Backend service templates
- ML/AI project templates

## 🤝 Contributing

To improve this universal container:
1. Fork the repository
2. Test with different project types
3. Add missing tools or languages
4. Optimize performance
5. Update documentation
6. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Report bugs or request features on [GitHub Issues](https://github.com/davidarule/UniversalClaudeCodeContainer/issues)
- **Documentation**: Check the detailed guides in the `.devcontainer/` and `.github/` directories
- **Setup Help**: Use the interactive `setup.py` script for guided installation

## 🎉 What's New

### Version 2.0 (Latest)
- ✅ **11 MCP Servers** including new Context7 vector database
- ✅ **16 IDE Support** from VS Code to Neovim
- ✅ **Interactive Setup Script** with step-by-step guidance
- ✅ **Individual MCP Selection** - choose only what you need
- ✅ **Enhanced Mobile Development** with Flutter, React Native, Android SDK
- ✅ **Advanced API Integration** via Composio platform
- ✅ **Semantic Search** capabilities with Context7/Upstash Vector

---

**Happy coding with Claude Code! 🚀**

This container is designed to be the ultimate development environment for Claude Code, supporting virtually any type of software development project with powerful AI assistance through MCP servers.