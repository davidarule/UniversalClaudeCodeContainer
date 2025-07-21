# MCP Servers Usage Guide

This comprehensive guide explains how to use each of the 11 MCP servers included in the Universal Claude Code Container. Each server enhances Claude Code's capabilities in different ways.

## 📋 Quick Reference

| Server | Purpose | API Required | Best For |
|--------|---------|--------------|----------|
| [GitHub](#1-github-server) | Repository management | GitHub PAT | Git workflows, issues, PRs |
| [File System](#2-file-system-server) | Advanced file ops | None | File management, search |
| [Sequential Thinking](#3-sequential-thinking-server) | Enhanced reasoning | None | Complex problem solving |
| [Puppeteer](#4-puppeteer-server) | Web automation | None | Web scraping, testing |
| [PostgreSQL](#5-postgresql-server) | Database access | Connection string | Database operations |
| [Memory Bank](#6-memory-bank-server) | Persistent memory | None | Context retention |
| [Context7](#7-context7-server) | Vector search | Upstash creds | Semantic search |
| [Notion](#8-notion-server) | Workspace integration | Composio API | Documentation sync |
| [Figma](#9-figma-server) | Design integration | Composio API | Design workflows |
| [Zapier](#10-zapier-server) | Automation | Composio API | Workflow automation |
| [Apidog](#11-apidog-server) | API testing | Apidog API | API development |

---

## 1. GitHub Server

**Purpose**: Complete GitHub integration for repository management, issue tracking, and collaboration.

### What You Can Do
- **Repository Management**: Clone, create, and manage repositories
- **Issue Tracking**: Create, update, and close issues
- **Pull Requests**: Create PRs, review code, merge changes
- **Release Management**: Create releases and manage tags
- **Search**: Find repositories, code, issues, and users
- **Collaboration**: Manage teams, permissions, and workflows

### Common Commands
```
# Repository operations
"Show me the latest commits in my main repository"
"Create a new issue titled 'Bug: Login not working'"
"List all open pull requests that need review"

# Code search
"Find all JavaScript files that use the 'useState' hook"
"Search for similar implementations of authentication"

# Project management
"Create a release for version 2.1.0 with changelog"
"Assign issue #42 to @username and add 'bug' label"
```

### Setup Requirements
- **GitHub Personal Access Token** with scopes:
  - `repo` (Full control of repositories)
  - `read:org` (Read organization membership)
  - `read:user` (Read user profile data)
  - `gist` (Create gists)
  - `workflow` (Update GitHub Actions)

### Best Practices
- Use descriptive commit messages
- Link issues to PRs for better tracking
- Utilize GitHub's search syntax for precise results
- Leverage automated workflows with GitHub Actions

---

## 2. File System Server

**Purpose**: Advanced file operations beyond standard Claude Code access.

### What You Can Do
- **File Operations**: Read, write, create, delete files and directories
- **Search**: Find files by name, content, or patterns
- **Directory Management**: List, create, and organize directories
- **File Watching**: Monitor file changes in real-time
- **Bulk Operations**: Process multiple files simultaneously

### Common Commands
```
# File operations
"Create a new directory called 'components' in src/"
"Find all TypeScript files that import React"
"Copy all .env files to a backup directory"

# Search operations
"Find all files containing 'TODO' comments"
"List all Python files larger than 100KB"
"Show me recently modified files in the project"

# Bulk operations
"Rename all .js files to .jsx in the components folder"
"Delete all node_modules directories in subdirectories"
```

### Setup Requirements
- **No API keys required**
- Uses local filesystem server built from source

### Best Practices
- Always backup important files before bulk operations
- Use specific patterns to avoid unintended file matches
- Leverage file watching for hot reload development
- Organize files logically for better project structure

---

## 3. Sequential Thinking Server

**Purpose**: Enhanced reasoning and problem-solving capabilities for complex tasks.

### What You Can Do
- **Step-by-Step Analysis**: Break down complex problems into manageable steps
- **Decision Trees**: Evaluate multiple solution paths
- **Logical Reasoning**: Apply formal logic to code problems
- **Pattern Recognition**: Identify design patterns and best practices
- **Architecture Planning**: Design system architecture systematically

### Common Commands
```
# Problem solving
"Help me design a scalable authentication system step by step"
"Analyze the trade-offs between SQL and NoSQL for this project"
"Break down this complex algorithm into smaller functions"

# Architecture decisions
"Plan the migration from monolith to microservices"
"Design a caching strategy for high-traffic endpoints"
"Evaluate different state management solutions for React"

# Code review
"Systematically review this code for potential issues"
"Suggest improvements following SOLID principles"
```

### Setup Requirements
- **No API keys required**
- Automatically enhances Claude's reasoning

### Best Practices
- Present complex problems clearly with context
- Ask for step-by-step breakdowns of difficult tasks
- Use for architectural decisions and code reviews
- Leverage for learning new concepts systematically

---

## 4. Puppeteer Server

**Purpose**: Web automation, scraping, and browser-based testing.

### What You Can Do
- **Web Scraping**: Extract data from websites
- **UI Testing**: Automate browser interactions
- **Screenshot Generation**: Capture web pages and elements
- **Performance Testing**: Analyze page load times and metrics
- **Form Automation**: Fill out and submit web forms

### Common Commands
```
# Web scraping
"Scrape the latest job postings from this tech job site"
"Extract product prices from this e-commerce page"
"Get all the headlines from this news website"

# Testing
"Test the login flow on my web application"
"Take screenshots of the homepage at different screen sizes"
"Check if all navigation links are working correctly"

# Automation
"Fill out this contact form with test data"
"Automate clicking through the onboarding flow"
"Monitor this page for changes every hour"
```

### Setup Requirements
- **No API keys required**
- Chrome/Chromium browser automatically included

### Best Practices
- Respect robots.txt and rate limits when scraping
- Use headless mode for better performance
- Add delays between actions to avoid detection
- Test on different viewport sizes for responsive design

---

## 5. PostgreSQL Server

**Purpose**: Direct database interactions, queries, and schema management.

### What You Can Do
- **Database Queries**: Execute SELECT, INSERT, UPDATE, DELETE operations
- **Schema Management**: Create and modify tables, indexes, constraints
- **Data Analysis**: Aggregate data and generate insights
- **Performance Optimization**: Analyze query performance and suggest improvements
- **Migration Management**: Handle database schema changes

### Common Commands
```
# Data queries
"Show me all users who signed up in the last 30 days"
"Find the top 10 products by sales volume"
"Get user activity statistics by month"

# Schema operations
"Create a new table for storing user preferences"
"Add an index on the email column for faster lookups"
"Show me the current database schema"

# Analysis
"Analyze which queries are slowest in the database"
"Suggest optimizations for this complex JOIN query"
"Generate a report of database growth over time"
```

### Setup Requirements
- **PostgreSQL connection string**: `postgresql://user:password@host:port/database`
- Database server must be accessible from container

### Best Practices
- Use prepared statements to prevent SQL injection
- Create indexes for frequently queried columns
- Backup database before schema changes
- Monitor query performance and optimize slow queries

---

## 6. Memory Bank Server

**Purpose**: Persistent memory and context retention across Claude Code sessions.

### What You Can Do
- **Context Persistence**: Remember project preferences and decisions
- **Learning Tracking**: Store information about technologies used
- **Project History**: Maintain project evolution and changes
- **Personal Preferences**: Remember coding style and preferences
- **Decision Documentation**: Keep track of architectural decisions

### Common Commands
```
# Context management
"Remember that I prefer TypeScript over JavaScript for this project"
"Save the decision to use Redux for state management"
"Note that we're using Material-UI for the component library"

# Preference tracking
"Remember my coding style preferences for Python projects"
"Save that I prefer functional components over class components"
"Note my preferred folder structure for React projects"

# Project documentation
"Remember the API endpoints and their purposes"
"Save the database schema decisions we made"
"Document why we chose this particular architecture"
```

### Setup Requirements
- **No API keys required**
- Automatically stores context locally

### Best Practices
- Regularly save important project decisions
- Document reasoning behind architectural choices
- Use for maintaining consistency across sessions
- Review stored context periodically for accuracy

---

## 7. Context7 Server

**Purpose**: Vector database for semantic search and contextual retrieval.

### What You Can Do
- **Semantic Search**: Find code by meaning, not just keywords
- **Code Similarity**: Discover similar code patterns and functions
- **Documentation Search**: Search through project documentation intelligently
- **Context Retrieval**: Get relevant context for large codebases
- **AI Recommendations**: Receive intelligent suggestions based on context

### Common Commands
```
# Semantic search
"Find code similar to this authentication function"
"Search for components that handle user input validation"
"Find documentation about API rate limiting"

# Code discovery
"Show me all functions that process payment data"
"Find examples of error handling patterns in this codebase"
"Locate components that use the same design pattern"

# Context analysis
"Analyze the relationships between these modules"
"Find the most relevant code for implementing feature X"
"Suggest improvements based on similar implementations"
```

### Setup Requirements
- **Upstash Vector Database**: REST URL and Token
- Create at [Upstash Console](https://console.upstash.com)

### Best Practices
- Index your most important project files
- Use descriptive queries for better results
- Regularly update the vector database with new code
- Leverage for code review and architecture analysis

---

## 8. Notion Server

**Purpose**: Workspace integration and documentation synchronization.

### What You Can Do
- **Documentation Sync**: Keep project docs in sync with Notion
- **Task Management**: Create and manage project tasks
- **Knowledge Base**: Build and maintain project knowledge
- **Team Collaboration**: Share information with team members
- **Project Planning**: Use Notion databases for project planning

### Common Commands
```
# Documentation
"Sync the API documentation to Notion page"
"Create a new project requirements document"
"Update the team knowledge base with new findings"

# Task management
"Create a task for implementing user authentication"
"Update the sprint planning board with new tickets"
"Mark the deployment checklist as completed"

# Collaboration
"Share the project roadmap with the team"
"Create a meeting notes template for standup meetings"
"Document the onboarding process for new developers"
```

### Setup Requirements
- **Composio API Key**: From [Composio Dashboard](https://app.composio.dev)
- Notion workspace access

### Best Practices
- Organize information in structured databases
- Use templates for consistent documentation
- Keep project documentation up to date
- Leverage Notion's powerful database features

---

## 9. Figma Server

**Purpose**: Design tool integration and asset management.

### What You Can Do
- **Asset Export**: Export design assets and components
- **Design Sync**: Keep designs in sync with implementation
- **Component Library**: Manage design system components
- **Collaboration**: Work with designers on implementation
- **Design Review**: Review and comment on designs

### Common Commands
```
# Asset management
"Export all icons from the design system Figma file"
"Get the latest mockups for the user dashboard"
"Download assets for the mobile app screens"

# Design sync
"Check if the button component matches the Figma design"
"Compare the implemented layout with the design"
"Get the exact colors and spacing from the design system"

# Collaboration
"Add a comment about implementation complexity"
"Mark this design as ready for development"
"Get design specifications for the new feature"
```

### Setup Requirements
- **Composio API Key**: From [Composio Dashboard](https://app.composio.dev)
- Figma account and file access

### Best Practices
- Maintain a consistent design system
- Regular sync between design and implementation
- Use Figma's developer handoff features
- Collaborate closely with design team

---

## 10. Zapier Server

**Purpose**: Cross-app automation and workflow integration.

### What You Can Do
- **Workflow Automation**: Create automated workflows between apps
- **Data Sync**: Keep data synchronized across platforms
- **Notification Systems**: Set up alerts and notifications
- **Integration Management**: Connect different tools and services
- **Process Automation**: Automate repetitive business processes

### Common Commands
```
# Automation setup
"Create a workflow to notify Slack when deployment completes"
"Set up automatic backup of code to Google Drive"
"Automate creating GitHub issues from support tickets"

# Data synchronization
"Sync customer data between CRM and database"
"Update project status in multiple project management tools"
"Keep team calendars synchronized across platforms"

# Notifications
"Send email notifications when CI/CD pipeline fails"
"Post deployment announcements to team channels"
"Alert team when critical errors occur in production"
```

### Setup Requirements
- **Composio API Key**: From [Composio Dashboard](https://app.composio.dev)
- Zapier account and connected apps

### Best Practices
- Start with simple workflows and gradually add complexity
- Test workflows thoroughly before going live
- Monitor workflow performance and success rates
- Document workflows for team understanding

---

## 11. Apidog Server

**Purpose**: API documentation, testing, and client generation.

### What You Can Do
- **API Documentation**: Create and maintain API documentation
- **API Testing**: Test endpoints and validate responses
- **Mock Servers**: Create mock APIs for development
- **Client Generation**: Generate client code for APIs
- **API Monitoring**: Monitor API performance and uptime

### Common Commands
```
# Documentation
"Generate API documentation from this OpenAPI spec"
"Create documentation for the new user endpoints"
"Update the API docs with the latest changes"

# Testing
"Test all user authentication endpoints"
"Validate that the API responses match the schema"
"Run the full API test suite and report results"

# Development
"Create a mock server for the payment API"
"Generate a TypeScript client for this API"
"Set up automated testing for API endpoints"
```

### Setup Requirements
- **Apidog API Key**: From [Apidog Dashboard](https://apidog.com)
- Access to API specifications

### Best Practices
- Keep API documentation up to date with implementations
- Use consistent naming conventions for endpoints
- Implement comprehensive testing for all endpoints
- Version your APIs properly for backward compatibility

---

## 🚀 Getting Started

### 1. Run the Setup Script
```bash
python3 setup.py
```

### 2. Select Your MCP Servers
Choose which servers you want to use based on your project needs:
- **Core Development**: GitHub, File System, Sequential Thinking
- **Database Projects**: PostgreSQL, Memory Bank, Context7
- **Web Projects**: Puppeteer, Apidog
- **Team Collaboration**: Notion, Figma, Zapier

### 3. Configure API Keys
Only provide keys for the servers you selected:
- Follow the setup URLs provided in the script
- Use environment variables for security
- Test connections after setup

### 4. Start Using MCP Servers
- Restart Claude Desktop after configuration
- Begin with simple commands to test functionality
- Gradually explore advanced features

## 🎯 Pro Tips

### Combining Servers
- **GitHub + Memory Bank**: Remember project decisions across sessions
- **Context7 + File System**: Semantic search across your entire codebase
- **Puppeteer + Apidog**: End-to-end testing of web APIs
- **Notion + Zapier**: Automated documentation workflows

### Performance Optimization
- Use specific queries for better results
- Cache frequently accessed data
- Combine related operations in single requests
- Monitor API usage and rate limits

### Security Best Practices
- Rotate API keys regularly
- Use environment variables for sensitive data
- Limit API key permissions to minimum required
- Monitor API usage for unusual activity

---

**Happy coding with enhanced Claude Code capabilities! 🚀**

This guide covers all 11 MCP servers. Each server significantly enhances Claude Code's abilities, making it the ultimate AI-powered development environment.