FROM mcr.microsoft.com/devcontainers/universal:2-linux

# Install additional packages and tools
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    # System essentials
    curl \
    wget \
    gnupg \
    lsb-release \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    # Build tools
    build-essential \
    cmake \
    ninja-build \
    ccache \
    pkg-config \
    autoconf \
    automake \
    libtool \
    # Version control
    git \
    git-lfs \
    subversion \
    mercurial \
    # C/C++ development
    gcc-12 \
    g++-12 \
    clang-15 \
    clang-format-15 \
    clang-tidy-15 \
    lldb-15 \
    valgrind \
    gdb \
    # Python development (Python 3.11 included in base)
    python3-pip \
    python3-venv \
    python3-dev \
    pipx \
    # Java development (JDK included in base)
    maven \
    gradle \
    # JavaScript/TypeScript (Node.js included in base)
    npm \
    yarn \
    pnpm \
    # Go development (Go included in base)
    gopls \
    # Rust development
    rustc \
    cargo \
    rustfmt \
    clippy \
    # Ruby development
    ruby-full \
    ruby-dev \
    # PHP development
    php8.2 \
    php8.2-cli \
    php8.2-dev \
    php8.2-mbstring \
    php8.2-xml \
    php8.2-curl \
    composer \
    # .NET development
    dotnet-sdk-8.0 \
    # Android development dependencies
    openjdk-17-jdk \
    unzip \
    lib32stdc++6 \
    lib32z1 \
    libc6-dev-i386 \
    # iOS development dependencies (for cross-platform tools)
    libssl-dev \
    libffi-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    # Database clients
    postgresql-client \
    mysql-client \
    sqlite3 \
    redis-tools \
    mongodb-clients \
    # Container tools
    docker.io \
    docker-compose \
    podman \
    # Cloud CLI tools
    awscli \
    azure-cli \
    # Kubernetes tools
    kubectl \
    helm \
    minikube \
    # Terraform
    terraform \
    # Web development
    httpie \
    jq \
    yq \
    # Performance tools
    htop \
    iotop \
    nethogs \
    sysstat \
    # Search tools
    ripgrep \
    fd-find \
    fzf \
    the-silver-searcher \
    # File tools
    tree \
    ncdu \
    bat \
    exa \
    # Terminal multiplexer
    tmux \
    screen \
    # Editors
    vim \
    neovim \
    emacs \
    nano \
    # Documentation tools
    pandoc \
    graphviz \
    # Security tools
    gnupg2 \
    pass \
    # Network tools
    curl \
    wget \
    nmap \
    netcat \
    tcpdump \
    # Compression tools
    zip \
    unzip \
    p7zip-full \
    # Image tools
    imagemagick \
    # Audio/Video tools
    ffmpeg \
    # LaTeX (optional, large)
    # texlive-full \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Install Google Cloud SDK
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \
    && apt-get update && apt-get install -y google-cloud-cli \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Set up alternatives for clang tools
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-15 100 \
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-15 100 \
    && update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-15 100 \
    && update-alternatives --install /usr/bin/clang-tidy clang-tidy /usr/bin/clang-tidy-15 100

# Install Android SDK and tools
ENV ANDROID_HOME=/opt/android-sdk \
    ANDROID_SDK_ROOT=/opt/android-sdk \
    PATH=${PATH}:/opt/android-sdk/cmdline-tools/latest/bin:/opt/android-sdk/platform-tools:/opt/android-sdk/build-tools/34.0.0

RUN mkdir -p ${ANDROID_HOME}/cmdline-tools && \
    cd ${ANDROID_HOME}/cmdline-tools && \
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip && \
    unzip commandlinetools-linux-11076708_latest.zip && \
    mv cmdline-tools latest && \
    rm commandlinetools-linux-11076708_latest.zip

# Accept Android SDK licenses and install components
RUN yes | ${ANDROID_HOME}/cmdline-tools/latest/bin/sdkmanager --licenses && \
    ${ANDROID_HOME}/cmdline-tools/latest/bin/sdkmanager \
    "platform-tools" \
    "platforms;android-34" \
    "platforms;android-33" \
    "platforms;android-32" \
    "build-tools;34.0.0" \
    "build-tools;33.0.1" \
    "emulator" \
    "system-images;android-34;google_apis;x86_64" \
    "system-images;android-33;google_apis;x86_64"

# Install Flutter
ENV FLUTTER_HOME=/opt/flutter \
    PATH=${PATH}:/opt/flutter/bin

RUN git clone https://github.com/flutter/flutter.git -b stable ${FLUTTER_HOME} && \
    ${FLUTTER_HOME}/bin/flutter precache && \
    ${FLUTTER_HOME}/bin/flutter config --enable-web --enable-linux-desktop && \
    ${FLUTTER_HOME}/bin/flutter doctor

# Install React Native CLI and Expo CLI
RUN npm install -g \
    @react-native-community/cli \
    @expo/cli \
    eas-cli

# Install Ionic CLI and Capacitor
RUN npm install -g \
    @ionic/cli \
    @capacitor/cli

# Install Cordova CLI
RUN npm install -g cordova

# Install global npm packages
RUN npm install -g \
    typescript \
    ts-node \
    nodemon \
    pm2 \
    prettier \
    eslint \
    @angular/cli \
    @vue/cli \
    create-react-app \
    create-next-app \
    @nestjs/cli \
    nx \
    lerna \
    webpack \
    webpack-cli \
    parcel \
    vite \
    jest \
    mocha \
    cypress \
    playwright \
    puppeteer \
    lighthouse \
    vercel \
    netlify-cli \
    firebase-tools \
    serverless \
    # Mobile development tools
    appium \
    appium-doctor \
    # PWA tools
    @pwa/cli \
    workbox-cli

# Install Python tools globally
RUN pipx install \
    poetry \
    pipenv \
    black \
    flake8 \
    mypy \
    pytest \
    tox \
    pre-commit \
    cookiecutter \
    jupyter \
    ipython \
    pandas \
    numpy \
    matplotlib \
    scikit-learn \
    tensorflow \
    torch \
    fastapi \
    django \
    flask \
    streamlit

# Install Rust tools
RUN cargo install \
    cargo-watch \
    cargo-edit \
    cargo-outdated \
    cargo-audit \
    sccache

# Install Go tools
RUN go install golang.org/x/tools/gopls@latest \
    && go install github.com/go-delve/delve/cmd/dlv@latest \
    && go install golang.org/x/lint/golint@latest \
    && go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest

# Install Ruby gems
RUN gem install \
    bundler \
    rails \
    sinatra \
    rspec \
    rubocop \
    pry

# Install PHP tools
RUN composer global require \
    phpunit/phpunit \
    squizlabs/php_codesniffer \
    phpstan/phpstan \
    friendsofphp/php-cs-fixer

# Install Haskell (optional, large)
# RUN curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh

# Install Nix package manager (optional)
# RUN curl -L https://nixos.org/nix/install | sh

# Create directories for various tools
RUN mkdir -p /home/codespace/.cache \
    && mkdir -p /home/codespace/.config \
    && mkdir -p /home/codespace/.local/share \
    && mkdir -p /opt/tools

# Set environment variables
ENV DEBIAN_FRONTEND=dialog \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PIPX_HOME=/usr/local/pipx \
    PIPX_BIN_DIR=/usr/local/bin \
    CARGO_HOME=/usr/local/cargo \
    RUSTUP_HOME=/usr/local/rustup \
    GOPATH=/go \
    COMPOSER_HOME=/usr/local/composer \
    GEM_HOME=/usr/local/bundle \
    BUNDLE_PATH=/usr/local/bundle \
    PATH="/usr/local/cargo/bin:/usr/local/go/bin:/go/bin:/usr/local/composer/vendor/bin:/usr/local/bundle/bin:${PATH}"

# Configure git
RUN git config --global init.defaultBranch main \
    && git config --global core.editor "code --wait" \
    && git config --global pull.rebase false

# Install oh-my-zsh and plugins
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended \
    && git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions \
    && git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting \
    && sed -i 's/plugins=(git)/plugins=(git docker docker-compose kubectl terraform aws gcloud azure golang node npm python pip rust cargo ruby rails composer laravel)/g' ~/.zshrc

# Switch to codespace user
USER codespace

# Set zsh as default shell
SHELL ["/bin/zsh", "-c"]

# Final working directory
WORKDIR /workspaces