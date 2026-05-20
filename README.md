<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>MG Advisory Finance OS</title>
    <link rel="stylesheet" href="/frontend/styles.css" />
  </head>
  <body>
    <section id="loginView" class="login-view">
      <div class="login-brand">
        <img class="brand-logo hero-logo" src="/frontend/assets/mg-strategic-finance-ai-logo.png" alt="MG Strategic Finance AI" />
        <p class="eyebrow">MG Advisory</p>
        <h1>Strategic Finance AI</h1>
        <p class="login-copy">Institutional business planning, debt analytics and transaction outputs in one controlled workspace.</p>
      </div>

      <form id="loginForm" class="login-card">
        <p class="eyebrow">Secure Access</p>
        <h2>Sign in</h2>
        <label for="licenseKey">License key</label>
        <input id="licenseKey" type="password" value="MG-ADVISORY-DEMO-2026" autocomplete="current-password" />
        <button type="submit">Enter workspace</button>
        <p id="loginMessage" class="message"></p>
      </form>
    </section>

    <main id="appView" class="app-shell hidden">
      <aside class="side-nav">
        <div>
          <div class="brand-row">
            <img class="brand-logo nav-logo" src="/frontend/assets/mg-strategic-finance-ai-logo.png" alt="MG Strategic Finance AI" />
            <div>
              <strong>Strategic Finance AI</strong>
              <span>Institutional SaaS</span>
            </div>
          </div>
          <nav class="nav-list">
            <button class="nav-item active" data-view="dashboardView">Dashboard</button>
            <button class="nav-item" data-view="libraryView">Project Library</button>
            <button class="nav-item" data-view="projectView">Active Project</button>
            <button class="nav-item" data-view="outputsView">Outputs</button>
          </nav>
        </div>
        <div class="nav-footer">
          <span id="licenseStatus">Unlocked</span>
          <button id="logoutButton" class="ghost-button">Sign out</button>
        </div>
      </aside>

      <section class="main-area">
        <header class="topbar">
          <div>
            <p class="eyebrow">Workspace</p>
            <h2 id="pageTitle">Dashboard</h2>
          </div>
          <div class="topbar-actions">
            <button id="refreshButton" class="secondary-button">Refresh</button>
            <button id="newProjectTopButton">New project</button>
          </div>
        </header>

        <section id="dashboardView" class="view active-view">
          <div class="metric-grid">
            <div class="metric-card">
              <span>Total projects</span>
              <strong id="projectCount">0</strong>
            </div>
            <div class="metric-card">
              <span>Active project</span>
              <strong id="activeProjectMetric">None</strong>
            </div>
            <div class="metric-card">
              <span>Excel model</span>
              <strong id="modelStatusMetric">Ready</strong>
            </div>
            <div class="metric-card">
              <span>AI layer</span>
              <strong id="aiStatusMetric">Checking</strong>
            </div>
          </div>

          <section class="workbench">
            <div class="panel wide">
              <div class="panel-head">
                <div>
                  <p class="eyebrow">Pipeline</p>
                  <h3>Recent dossiers</h3>
                </div>
                <button class="secondary-button" data-view-button="libraryView">Open library</button>
              </div>
              <div id="recentProjects" class="project-table"></div>
            </div>

            <div class="panel">
              <p class="eyebrow">System</p>
              <h3>Modules</h3>
              <div class="module-list">
                <div><span>BP Model</span><strong>Online</strong></div>
                <div><span>Debt Engine</span><strong>Online</strong></div>
                <div><span>Data Room</span><strong>Online</strong></div>
                <div><span>Claude Brief</span><strong id="aiModuleStatus">Checking</strong></div>
              </div>
            </div>
          </section>
        </section>

        <section id="libraryView" class="view">
          <section class="workbench">
            <div class="panel">
              <p class="eyebrow">Create</p>
              <h3>New investment dossier</h3>
              <label for="companyName">Company</label>
              <input id="companyName" placeholder="Portfolio Company Ltd" />
              <label for="projectType">Project type</label>
              <select id="projectType">
                <option>Investment case</option>
                <option>Transaction services</option>
                <option>Restructuring</option>
                <option>Lender reporting</option>
                <option>M&A sell-side</option>
              </select>
              <label for="currency">Currency</label>
              <select id="currency">
                <option>EUR</option>
                <option>USD</option>
                <option>GBP</option>
                <option>AED</option>
              </select>
              <button id="createProjectButton" class="full-button">Create dossier</button>
              <p id="createMessage" class="message"></p>
            </div>

            <div class="panel wide">
              <div class="panel-head">
                <div>
                  <p class="eyebrow">Library</p>
                  <h3>Project dossiers</h3>
                </div>
                <input id="projectSearch" class="search-input" placeholder="Search company or type" />
              </div>
              <div id="projectList" class="project-table"></div>
            </div>
          </section>
        </section>

        <section id="projectView" class="view">
          <div id="emptyProjectState" class="empty-state">
            <h3>No active project selected</h3>
            <button data-view-button="libraryView">Open project library</button>
          </div>

          <div id="projectWorkspace" class="hidden">
            <section class="project-hero">
              <div>
                <p class="eyebrow">Active Dossier</p>
                <h3 id="activeProjectName">Project</h3>
                <p id="activeProjectMeta" class="muted"></p>
              </div>
              <div class="hero-actions">
                <button id="generateBpButton">Generate BP model</button>
                <button id="downloadBpButton" class="secondary-button">Download</button>
              </div>
            </section>

            <section class="workbench">
              <div class="panel wide">
                <p class="eyebrow">Data Room</p>
                <h3>Financial source files</h3>
                <div class="upload-zone">
                  <input id="fileInput" type="file" accept=".pdf,.xlsx,.xlsm,.csv" />
                  <button id="uploadButton">Upload and normalize</button>
                </div>
                <div id="uploadResult" class="result-box"></div>
              </div>

              <div class="panel">
                <p class="eyebrow">Coverage</p>
                <h3>Expected sources</h3>
                <div class="checklist">
                  <span>Audited accounts PDF</span>
                  <span>Management accounts XLSX</span>
                  <span>Trial balance</span>
                  <span>Aged receivables</span>
                  <span>Aged payables</span>
                  <span>Debt schedule</span>
                  <span>Budget / forecast</span>
                </div>
              </div>
            </section>
          </div>
        </section>

        <section id="outputsView" class="view">
          <section class="workbench">
            <div class="panel wide">
              <p class="eyebrow">Generation</p>
              <h3>Institutional deliverables</h3>
              <div class="output-grid">
                <button id="generateBpOutputButton">Excel BP model</button>
                <button id="aiBriefButton" class="secondary-button">AI project brief</button>
                <button class="disabled-button" disabled>QoE pack</button>
                <button class="disabled-button" disabled>Debt covenant pack</button>
                <button class="disabled-button" disabled>Lender presentation</button>
                <button class="disabled-button" disabled>IM / M&A deck</button>
              </div>
              <div id="outputResult" class="result-box"></div>
            </div>

            <div class="panel">
              <p class="eyebrow">Templates</p>
              <h3>Available references</h3>
              <div class="module-list">
                <div><span>Book Schemas PPTX</span><strong>Loaded</strong></div>
                <div><span>Karesi IM PDF</span><strong>Loaded</strong></div>
                <div><span>MG Excel BP V2</span><strong>Active</strong></div>
              </div>
            </div>
          </section>
        </section>
      </section>
    </main>

    <script src="/frontend/app.js"></script>
  </body>
</html>
