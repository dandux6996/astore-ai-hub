<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Astore Intelligence Platform - ESG-Driven Category Management</title>
    <style>
        :root {
            --color-primary: #218085;
            --color-primary-dark: #1a6468;
            --color-accent: #32B8C6;
            --color-success: #21A67F;
            --color-warning: #E68161;
            --color-danger: #C0152F;
            --color-bg: #FCFCF9;
            --color-surface: #FFFFFF;
            --color-text: #1F2121;
            --color-text-secondary: #626C71;
            --color-border: rgba(94, 82, 64, 0.15);
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
            --radius: 12px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #e8eef3 100%);
            color: var(--color-text);
            line-height: 1.6;
        }

        .header {
            background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
            color: white;
            padding: 2.5rem 2rem;
            box-shadow: var(--shadow-md);
        }

        .header-content {
            max-width: 1400px;
            margin: 0 auto;
        }

        .logo-section {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .logo {
            width: 50px;
            height: 50px;
            background: white;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: var(--color-primary);
            font-size: 1.5rem;
        }

        h1 {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            letter-spacing: -0.5px;
        }

        .subtitle {
            font-size: 1.1rem;
            opacity: 0.95;
            font-weight: 400;
        }

        .value-banner {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 1.5rem;
            border-radius: var(--radius);
            margin-top: 1.5rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .value-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
        }

        .value-item {
            text-align: center;
        }

        .value-number {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }

        .value-label {
            font-size: 0.9rem;
            opacity: 0.9;
        }

        .container {
            max-width: 1400px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        .tabs {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 2rem;
            overflow-x: auto;
            padding-bottom: 0.5rem;
        }

        .tab-btn {
            background: var(--color-surface);
            border: 2px solid var(--color-border);
            padding: 0.875rem 1.5rem;
            border-radius: var(--radius);
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            white-space: nowrap;
            color: var(--color-text);
        }

        .tab-btn:hover {
            border-color: var(--color-primary);
            background: rgba(33, 128, 133, 0.05);
        }

        .tab-btn.active {
            background: var(--color-primary);
            color: white;
            border-color: var(--color-primary);
        }

        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: block;
        }

        .card {
            background: var(--color-surface);
            border-radius: var(--radius);
            padding: 2rem;
            box-shadow: var(--shadow-sm);
            margin-bottom: 1.5rem;
            border: 1px solid var(--color-border);
        }

        .card h2 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            color: var(--color-primary);
        }

        .card-subtitle {
            color: var(--color-text-secondary);
            font-size: 0.95rem;
            margin-bottom: 1.5rem;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--color-text);
            font-size: 0.9rem;
        }

        select, input, textarea {
            width: 100%;
            padding: 0.75rem 1rem;
            border: 2px solid var(--color-border);
            border-radius: 8px;
            font-size: 0.95rem;
            transition: all 0.2s;
            font-family: inherit;
            background: var(--color-surface);
        }

        select:focus, input:focus, textarea:focus {
            outline: none;
            border-color: var(--color-primary);
            box-shadow: 0 0 0 3px rgba(33, 128, 133, 0.1);
        }

        textarea {
            resize: vertical;
            min-height: 100px;
        }

        .btn-primary {
            background: var(--color-primary);
            color: white;
            border: none;
            padding: 0.875rem 2rem;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            width: 100%;
            margin-top: 1rem;
        }

        .btn-primary:hover {
            background: var(--color-primary-dark);
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(33, 128, 133, 0.25);
        }

        .btn-primary:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }

        .loading {
            display: none;
            text-align: center;
            padding: 2rem;
        }

        .loading.active {
            display: block;
        }

        .spinner {
            border: 3px solid rgba(33, 128, 133, 0.1);
            border-top: 3px solid var(--color-primary);
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .result {
            background: rgba(33, 128, 133, 0.05);
            border-left: 4px solid var(--color-primary);
            padding: 1.5rem;
            border-radius: 8px;
            margin-top: 1.5rem;
            line-height: 1.8;
        }

        .result h3 {
            color: var(--color-primary);
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
            font-size: 1.2rem;
        }

        .result h4 {
            color: var(--color-text);
            margin-top: 1rem;
            margin-bottom: 0.5rem;
            font-size: 1rem;
        }

        .result ul, .result ol {
            margin-left: 1.5rem;
            margin-bottom: 1rem;
        }

        .result li {
            margin-bottom: 0.5rem;
        }

        .result strong {
            color: var(--color-primary);
        }

        .metric-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .metric-card {
            background: linear-gradient(135deg, rgba(33, 128, 133, 0.08) 0%, rgba(50, 184, 198, 0.08) 100%);
            padding: 1.25rem;
            border-radius: 10px;
            border: 1px solid rgba(33, 128, 133, 0.15);
        }

        .metric-value {
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--color-primary);
            margin-bottom: 0.25rem;
        }

        .metric-label {
            font-size: 0.85rem;
            color: var(--color-text-secondary);
            font-weight: 500;
        }

        .insight-badge {
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }

        .badge-esg {
            background: rgba(33, 166, 127, 0.15);
            color: var(--color-success);
        }

        .badge-cost {
            background: rgba(230, 129, 97, 0.15);
            color: var(--color-warning);
        }

        .badge-risk {
            background: rgba(192, 21, 47, 0.15);
            color: var(--color-danger);
        }

        .grid-2 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .info-box {
            background: linear-gradient(135deg, rgba(50, 184, 198, 0.05) 0%, rgba(33, 128, 133, 0.05) 100%);
            padding: 1.25rem;
            border-radius: 10px;
            border-left: 4px solid var(--color-accent);
            margin-bottom: 1rem;
        }

        .info-box strong {
            color: var(--color-primary);
            display: block;
            margin-bottom: 0.5rem;
        }

        @media (max-width: 768px) {
            .header {
                padding: 1.5rem 1rem;
            }

            h1 {
                font-size: 1.5rem;
            }

            .subtitle {
                font-size: 0.95rem;
            }

            .container {
                padding: 0 1rem;
            }

            .tabs {
                flex-direction: column;
            }

            .value-grid {
                grid-template-columns: 1fr;
            }

            .metric-grid {
                grid-template-columns: 1fr;
            }
        }

        .footer {
            text-align: center;
            padding: 2rem;
            color: var(--color-text-secondary);
            font-size: 0.9rem;
            margin-top: 3rem;
        }

        .api-note {
            background: rgba(230, 129, 97, 0.1);
            border: 1px solid rgba(230, 129, 97, 0.3);
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            font-size: 0.9rem;
            color: var(--color-text-secondary);
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <div class="logo-section">
                <div class="logo">AS</div>
                <div>
                    <h1>Astore Intelligence Platform</h1>
                    <div class="subtitle">ESG-Driven Category Management for Hospitality Services</div>
                </div>
            </div>
            <div class="value-banner">
                <div class="value-grid">
                    <div class="value-item">
                        <div class="value-number">€12M+</div>
                        <div class="value-label">Potential Annual Savings</div>
                    </div>
                    <div class="value-item">
                        <div class="value-number">35%</div>
                        <div class="value-label">Carbon Reduction Target</div>
                    </div>
                    <div class="value-item">
                        <div class="value-number">95%</div>
                        <div class="value-label">Supplier ESG Compliance</div>
                    </div>
                    <div class="value-item">
                        <div class="value-number">Real-time</div>
                        <div class="value-label">Market Intelligence</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('intelligence')">🔔 Intelligence Brief</button>
            <button class="tab-btn" onclick="switchTab('esg-impact')">🌱 ESG Impact Dashboard</button>
            <button class="tab-btn" onclick="switchTab('category-strategy')">📊 Category Strategy</button>
            <button class="tab-btn" onclick="switchTab('supplier-intelligence')">🔍 Supplier Intelligence</button>
            <button class="tab-btn" onclick="switchTab('tender-prep')">📋 Tender Preparation</button>
        </div>

        <!-- TAB 1: INDUSTRY & CATEGORY INTELLIGENCE -->
        <div id="intelligence" class="tab-content active">
            <div class="card">
                <h2>Industry & Category Intelligence</h2>
                <p class="card-subtitle">Real-time market intelligence, trends, and procurement-relevant insights across hospitality services</p>

                <div class="api-note">
                    ⚠️ <strong>Demo Mode:</strong> To activate live AI intelligence, add your Perplexity API key in the code (line 284). <a href="https://www.perplexity.ai/settings/api" target="_blank">Get your key here</a>.
                </div>

                <div class="form-group">
                    <label>Focus Area</label>
                    <select id="intel-focus">
                        <option value="Hospitality Market & Hotels">Hospitality Market &amp; Hotels</option>
                        <option value="Procurement & Sourcing">Procurement &amp; Sourcing</option>
                        <option value="Housekeeping & Cleaning Services">Housekeeping &amp; Cleaning Services</option>
                        <option value="Laundry & Textile Services">Laundry &amp; Textile Services</option>
                        <option value="Energy & Utilities">Energy &amp; Utilities</option>
                        <option value="Waste Management & Circular Economy">Waste Management &amp; Circular Economy</option>
                        <option value="ESG, Sustainability & Decarbonisation">ESG, Sustainability &amp; Decarbonisation</option>
                        <option value="Regulation & Policy">Regulation &amp; Policy</option>
                        <option value="Labour & Outsourced Services">Labour &amp; Outsourced Services</option>
                    </select>
                </div>

                <div class="grid-2">
                    <div class="form-group">
                        <label>Geographic Scope</label>
                        <select id="intel-geography">
                            <option value="Global">Global</option>
                            <option value="Europe">Europe</option>
                            <option value="UK">UK</option>
                            <option value="DACH">DACH</option>
                            <option value="Poland">Poland</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label>Time Horizon</label>
                        <select id="intel-timeframe">
                            <option value="Last 24 hours">Last 24 hours</option>
                            <option value="Last 7 days">Last 7 days</option>
                            <option value="Last 30 days">Last 30 days</option>
                        </select>
                    </div>
                </div>

                <button class="btn-primary" onclick="generateIntelligence()">Generate Intelligence Brief</button>

                <div id="intel-loading" class="loading">
                    <div class="spinner"></div>
                    <p>Gathering latest intelligence and market insights...</p>
                </div>

                <div id="intel-result"></div>
            </div>
        </div>

        <!-- TAB 2: ESG IMPACT DASHBOARD -->
        <div id="esg-impact" class="tab-content">
            <div class="card">
                <h2>ESG Impact & Decarbonisation Dashboard</h2>
                <p class="card-subtitle">Track and optimize sustainability performance across services categories - aligned with CSRD 2026 compliance requirements</p>

                <div class="api-note">
                    ⚠️ <strong>Demo Mode:</strong> To activate live AI intelligence, add your Perplexity API key in the code (line 284). <a href="https://www.perplexity.ai/settings/api" target="_blank">Get your key here</a>.
                </div>

                <div class="metric-grid">
                    <div class="metric-card">
                        <div class="metric-value">24.5 tCO₂</div>
                        <div class="metric-label">Scope 3 Emissions (Services)</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">€185K</div>
                        <div class="metric-label">ESG-Linked Cost Savings YTD</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">78%</div>
                        <div class="metric-label">Suppliers with PCF Data</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">12</div>
                        <div class="metric-label">Local/Diverse Suppliers</div>
                    </div>
                </div>

                <div class="form-group">
                    <label>Service Category</label>
                    <select id="esg-category">
                        <option value="Housekeeping Services">Housekeeping Services</option>
                        <option value="Laundry & Textile Services">Laundry &amp; Textile Services</option>
                        <option value="Energy Management Services">Energy Management Services</option>
                        <option value="Waste Management & Circular Economy">Waste Management &amp; Circular Economy</option>
                        <option value="Food & Beverage Supply Chain">Food &amp; Beverage Supply Chain</option>
                    </select>
                </div>

                <div class="form-group">
                    <label>Region</label>
                    <select id="esg-region">
                        <option value="DACH">DACH (Germany, Austria, Switzerland)</option>
                        <option value="UK">United Kingdom</option>
                        <option value="Poland">Poland</option>
                        <option value="Europe">Europe-wide</option>
                    </select>
                </div>

                <div class="form-group">
                    <label>ESG Focus Area</label>
                    <select id="esg-focus">
                        <option value="Carbon Footprint & Decarbonisation">Carbon Footprint &amp; Decarbonisation</option>
                        <option value="Circular Economy & Waste Reduction">Circular Economy &amp; Waste Reduction</option>
                        <option value="Ethical Labor & Human Rights">Ethical Labor &amp; Human Rights</option>
                        <option value="Supply Chain Transparency">Supply Chain Transparency</option>
                        <option value="Renewable Energy Adoption">Renewable Energy Adoption</option>
                    </select>
                </div>

                <button class="btn-primary" onclick="generateESGInsight()">Generate ESG Insight Report</button>

                <div id="esg-loading" class="loading">
                    <div class="spinner"></div>
                    <p>Analyzing ESG data and market trends...</p>
                </div>

                <div id="esg-result"></div>
            </div>
        </div>

        <!-- TAB 2: CATEGORY STRATEGY -->
        <div id="category-strategy" class="tab-content">
            <div class="card">
                <h2>AI-Powered Category Strategy</h2>
                <p class="card-subtitle">Generate data-driven strategies that balance cost optimization, service quality, and ESG objectives</p>

                <div class="grid-2">
                    <div class="form-group">
                        <label>Service Category</label>
                        <select id="strategy-category">
                            <option value="Housekeeping Services">Housekeeping Services</option>
                            <option value="Laundry & Textile Services">Laundry &amp; Textile Services</option>
                            <option value="Energy Management Services">Energy Management Services</option>
                            <option value="Waste Management Services">Waste Management Services</option>
                            <option value="Facilities Maintenance">Facilities Maintenance</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label>Region</label>
                        <select id="strategy-region">
                            <option value="DACH">DACH</option>
                            <option value="UK">UK</option>
                            <option value="Poland">Poland</option>
                            <option value="Europe">Europe</option>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label>Primary Objective</label>
                    <select id="strategy-objective">
                        <option value="ESG Improvement & Decarbonisation">ESG Improvement &amp; Decarbonisation</option>
                        <option value="Cost Optimization (with ESG constraints)">Cost Optimization (with ESG constraints)</option>
                        <option value="Supplier Consolidation">Supplier Consolidation</option>
                        <option value="Risk Mitigation">Risk Mitigation</option>
                        <option value="Service Quality Enhancement">Service Quality Enhancement</option>
                    </select>
                </div>

                <div class="form-group">
                    <label>Current Situation & Challenges</label>
                    <textarea id="strategy-context" placeholder="E.g., Currently 8 housekeeping suppliers across DACH with inconsistent ESG reporting. Labor shortages in Q4 2025. No Scope 3 data available. Seeking to reduce suppliers to 3-4 while improving carbon transparency..."></textarea>
                </div>

                <button class="btn-primary" onclick="generateStrategy()">Generate Category Strategy</button>

                <div id="strategy-loading" class="loading">
                    <div class="spinner"></div>
                    <p>Building strategic recommendations...</p>
                </div>

                <div id="strategy-result"></div>
            </div>
        </div>

        <!-- TAB 3: SUPPLIER INTELLIGENCE -->
        <div id="supplier-intelligence" class="tab-content">
            <div class="card">
                <h2>Supplier Intelligence & ESG Scoring</h2>
                <p class="card-subtitle">Deep-dive analysis of supplier capabilities, ESG credentials, and market positioning</p>

                <div class="form-group">
                    <label>Supplier Name</label>
                    <input type="text" id="supplier-name" placeholder="E.g., ISS Facility Services, Ecolab, Bunzl">
                </div>

                <div class="grid-2">
                    <div class="form-group">
                        <label>Service Category</label>
                        <select id="supplier-category">
                            <option value="Housekeeping Services">Housekeeping Services</option>
                            <option value="Laundry Services">Laundry Services</option>
                            <option value="Energy Management">Energy Management</option>
                            <option value="Waste Management">Waste Management</option>
                            <option value="Cleaning Chemicals">Cleaning Chemicals</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label>Region</label>
                        <select id="supplier-region">
                            <option value="DACH">DACH</option>
                            <option value="UK">UK</option>
                            <option value="Poland">Poland</option>
                            <option value="Europe">Europe</option>
                        </select>
                    </div>
                </div>

                <button class="btn-primary" onclick="analyzeSupplier()">Analyze Supplier</button>

                <div id="supplier-loading" class="loading">
                    <div class="spinner"></div>
                    <p>Gathering supplier intelligence and ESG data...</p>
                </div>

                <div id="supplier-result"></div>
            </div>

            <div class="card">
                <h2>Discover New Suppliers</h2>
                <p class="card-subtitle">Find pre-vetted suppliers with strong ESG credentials in your target markets</p>

                <div class="grid-2">
                    <div class="form-group">
                        <label>Service Category</label>
                        <select id="discover-category">
                            <option value="Housekeeping Services">Housekeeping Services</option>
                            <option value="Laundry Services">Laundry Services</option>
                            <option value="Waste Management">Waste Management</option>
                            <option value="Energy Management">Energy Management</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label>Region</label>
                        <select id="discover-region">
                            <option value="DACH">DACH</option>
                            <option value="UK">UK</option>
                            <option value="Poland">Poland</option>
                        </select>
                    </div>
                </div>

                <button class="btn-primary" onclick="discoverSuppliers()">Find Suppliers</button>

                <div id="discover-loading" class="loading">
                    <div class="spinner"></div>
                    <p>Searching supplier database...</p>
                </div>

                <div id="discover-result"></div>
            </div>
        </div>

        <!-- TAB 4: TENDER PREPARATION -->
        <div id="tender-prep" class="tab-content">
            <div class="card">
                <h2>AI Tender Preparation Assistant</h2>
                <p class="card-subtitle">Generate RFI/RFP templates with ESG KPIs and evaluation criteria tailored to your category and region</p>

                <div class="grid-2">
                    <div class="form-group">
                        <label>Service Category</label>
                        <select id="tender-category">
                            <option value="Housekeeping Services">Housekeeping Services</option>
                            <option value="Laundry & Textile Services">Laundry &amp; Textile Services</option>
                            <option value="Energy Management Services">Energy Management Services</option>
                            <option value="Waste Management Services">Waste Management Services</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label>Region</label>
                        <select id="tender-region">
                            <option value="DACH">DACH</option>
                            <option value="UK">UK</option>
                            <option value="Poland">Poland</option>
                            <option value="Multi-region">Multi-region</option>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label>Tender Type</label>
                    <select id="tender-type">
                        <option value="RFI (Request for Information)">RFI (Request for Information)</option>
                        <option value="RFP (Request for Proposal)">RFP (Request for Proposal)</option>
                        <option value="Supplier Evaluation Scorecard">Supplier Evaluation Scorecard</option>
                        <option value="ESG Questionnaire">ESG Questionnaire</option>
                    </select>
                </div>

                <div class="form-group">
                    <label>Key Requirements & Context</label>
                    <textarea id="tender-context" placeholder="E.g., Seeking single supplier for housekeeping across 25 hotels in DACH. Must have ISO 14001, living wage commitment, and carbon reporting capability. Contract value €2.5M annually..."></textarea>
                </div>

                <button class="btn-primary" onclick="generateTender()">Generate Tender Document</button>

                <div id="tender-loading" class="loading">
                    <div class="spinner"></div>
                    <p>Creating tender documentation...</p>
                </div>

                <div id="tender-result"></div>
            </div>
        </div>
    </div>

    <div class="footer">
        <p><strong>Astore Intelligence Platform</strong> | Powered by AI | Built for Category Managers</p>
        <p style="margin-top: 0.5rem; font-size: 0.85rem;">Demonstrating AI-augmented procurement for services categories in hospitality</p>
    </div>

    <script>
        // Replace this with your actual Perplexity API key
        const PPLX_API_KEY = "YOUR_API_KEY_HERE";
        const API_URL = "https://api.perplexity.ai/chat/completions";

        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            
            document.getElementById(tabId).classList.add('active');
            event.target.classList.add('active');
        }

        async function callPerplexityAPI(prompt) {
            if (PPLX_API_KEY === "YOUR_API_KEY_HERE") {
                return `<div class="info-box">
                    <strong>⚠️ Demo Mode</strong>
                    This platform uses Perplexity AI to generate real-time insights. To see live results, please add your API key in the code (line 284).
                    <br><br>
                    Get your free API key at: <a href="https://www.perplexity.ai/settings/api" target="_blank">https://www.perplexity.ai/settings/api</a>
                    <br><br>
                    <strong>What this feature would show:</strong>
                    <ul>
                        <li>Real-time market intelligence and trends</li>
                        <li>Supplier ESG performance data</li>
                        <li>Decarbonisation strategies specific to your category</li>
                        <li>Regulatory compliance insights (CSRD, CSDD)</li>
                        <li>Actionable recommendations with cost impact</li>
                    </ul>
                </div>`;
            }

            try {
                const response = await fetch(API_URL, {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${PPLX_API_KEY}`,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        model: "sonar-pro",
                        messages: [{role: "user", content: prompt}],
                        temperature: 0.2
                    })
                });

                const data = await response.json();
                return formatResponse(data.choices[0].message.content);
            } catch (error) {
                return `<div class="info-box" style="border-color: var(--color-danger);">
                    <strong>Error:</strong> ${error.message}
                    <br><br>Please check your API key and internet connection.
                </div>`;
            }
        }

        function formatResponse(text) {
            text = text.replace(/### (.*?)(\n|$)/g, '<h3>$1</h3>');
            text = text.replace(/## (.*?)(\n|$)/g, '<h3>$1</h3>');
            text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            text = text.replace(/\n\n/g, '<br><br>');
            text = text.replace(/- (.*?)(\n|$)/g, '<li>$1</li>');
            text = text.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');
            return text;
        }

        async function generateESGInsight() {
            const category = document.getElementById('esg-category').value;
            const region = document.getElementById('esg-region').value;
            const focus = document.getElementById('esg-focus').value;

            const loadingDiv = document.getElementById('esg-loading');
            const resultDiv = document.getElementById('esg-result');

            loadingDiv.classList.add('active');
            resultDiv.innerHTML = '';

            const prompt = `As an ESG procurement expert for Accor's Astore division, analyze the following:

**Category:** ${category}
**Region:** ${region}
**Focus Area:** ${focus}

Provide a concise executive report (2026 context) covering:

**1. ESG PERFORMANCE BASELINE**
- Current industry carbon intensity (per service unit/transaction)
- Typical Scope 3 emissions contribution from this category
- Key ESG risks in this category (labor, environment, compliance)

**2. DECARBONISATION OPPORTUNITIES**
- Top 3 high-impact interventions to reduce emissions
- Expected carbon reduction (% and tCO₂e)
- Cost implications (€ savings or investment needed)

**3. SUPPLIER ESG REQUIREMENTS**
- Must-have certifications and credentials
- Key ESG KPIs to track (aligned with CSRD 2026)
- Product Carbon Footprint (PCF) data availability

**4. REGULATORY & COMPLIANCE**
- Relevant 2026 regulations (CSRD, CSDD, PPWR)
- Regional compliance specifics for ${region}

**5. IMMEDIATE ACTION ITEMS**
- What to do this quarter (3 actions)
- How to measure success (specific KPIs)

Focus on ACTIONABLE, QUANTIFIED insights. Cite recent sources where possible.`;

            const result = await callPerplexityAPI(prompt);
            
            loadingDiv.classList.remove('active');
            resultDiv.innerHTML = `<div class="result">
                <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
                    <span class="insight-badge badge-esg">ESG Priority</span>
                    <span class="insight-badge badge-cost">Cost Impact</span>
                </div>
                ${result}
            </div>`;
        }

        async function generateStrategy() {
            const category = document.getElementById('strategy-category').value;
            const region = document.getElementById('strategy-region').value;
            const objective = document.getElementById('strategy-objective').value;
            const context = document.getElementById('strategy-context').value;

            const loadingDiv = document.getElementById('strategy-loading');
            const resultDiv = document.getElementById('strategy-result');

            loadingDiv.classList.add('active');
            resultDiv.innerHTML = '';

            const prompt = `As an Astore Category Manager for Accor, develop a strategic action plan:

**Category:** ${category}
**Region:** ${region}
**Objective:** ${objective}
**Current Situation:** ${context}

Provide an executive-ready strategy document:

**EXECUTIVE SUMMARY** (3 sentences)
- Current state, goal, expected impact

**SITUATION ANALYSIS**
- Spend baseline (estimate typical hotel spend in this category)
- Supplier landscape (concentration, maturity)
- Key pain points
- ESG compliance gaps

**STRATEGIC OBJECTIVES** (SMART goals for 12 months)
1. Cost/value objective (€ target)
2. ESG objective (carbon, compliance, diversity)
3. Operational objective (quality, risk)

**ACTION ROADMAP**

**Q1-Q2 (Immediate)**
- 3-4 specific actions with owners and timelines
- Expected impact (€, tCO₂e, or qualitative)

**Q3-Q4 (Build)**
- 3-4 next-phase actions
- Dependencies and risks

**SUCCESS METRICS**
- Financial KPIs (cost savings, avoidance)
- ESG KPIs (carbon, compliance, supplier diversity)
- Operational KPIs (SLA, quality scores)

**RISK MITIGATION**
- Top 3 risks and mitigation plans

Focus on PRACTICAL, IMPLEMENTABLE strategies. Be specific about numbers and timelines.`;

            const result = await callPerplexityAPI(prompt);
            
            loadingDiv.classList.remove('active');
            resultDiv.innerHTML = `<div class="result">${result}</div>`;
        }

        async function analyzeSupplier() {
            const name = document.getElementById('supplier-name').value;
            const category = document.getElementById('supplier-category').value;
            const region = document.getElementById('supplier-region').value;

            if (!name.trim()) {
                alert('Please enter a supplier name');
                return;
            }

            const loadingDiv = document.getElementById('supplier-loading');
            const resultDiv = document.getElementById('supplier-result');

            loadingDiv.classList.add('active');
            resultDiv.innerHTML = '';

            const prompt = `Provide detailed intelligence on this supplier for Accor procurement:

**Supplier:** ${name}
**Category:** ${category}
**Region:** ${region}

Generate a comprehensive supplier profile:

**COMPANY OVERVIEW**
- Headquarters, size (revenue, employees)
- Market position in hospitality
- Geographic coverage (especially ${region})
- Key hospitality clients (if known)

**SERVICE CAPABILITIES**
- Core offerings in ${category}
- Technology/innovation capabilities
- Quality certifications (ISO, etc.)

**ESG PERFORMANCE** (Critical for 2026)
- Carbon commitments (SBTi, net zero targets)
- Environmental certifications (ISO 14001, etc.)
- Social/labor practices (living wage, diversity)
- ESG reporting maturity (CDP, EcoVadis, etc.)
- Product Carbon Footprint (PCF) data availability

**FINANCIAL STABILITY**
- Revenue trend
- Credit rating or financial health indicators
- Investment in sustainability

**HOSPITALITY EXPERIENCE**
- Years serving hotel sector
- Notable hotel partnerships
- Understanding of hospitality operations

**STRENGTHS & RISKS**
- Top 3 competitive advantages
- Top 3 risk factors (financial, operational, reputational)

**NEGOTIATION INSIGHTS**
- Market position (pricing power)
- Differentiators to leverage
- Potential pressure points

**RECOMMENDATION**
- Tier classification (Strategic / Preferred / Approved / Caution)
- Ideal contract structure
- Next steps for engagement

Use current 2026 data where available. Be specific and cite sources.`;

            const result = await callPerplexityAPI(prompt);
            
            loadingDiv.classList.remove('active');
            resultDiv.innerHTML = `<div class="result">
                <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
                    <span class="insight-badge badge-esg">ESG Verified</span>
                    <span class="insight-badge badge-risk">Risk Assessed</span>
                </div>
                ${result}
            </div>`;
        }

        async function discoverSuppliers() {
            const category = document.getElementById('discover-category').value;
            const region = document.getElementById('discover-region').value;

            const loadingDiv = document.getElementById('discover-loading');
            const resultDiv = document.getElementById('discover-result');

            loadingDiv.classList.add('active');
            resultDiv.innerHTML = '';

            const prompt = `Identify top suppliers for Accor's Astore procurement:

**Category:** ${category}
**Region:** ${region}

Provide a shortlist of 6-8 suppliers (mix of established and emerging):

For each supplier include:

**SUPPLIER NAME**
- **Coverage:** Geographic reach (local vs. international)
- **Size:** Revenue estimate, employee count
- **Hospitality Focus:** % of business from hotels, key clients
- **ESG Credentials:** Key certifications, carbon commitments
- **Strengths:** 2-3 differentiators relevant to hospitality
- **Typical Pricing:** Premium / Mid-range / Competitive
- **Website:** URL

Group into:
1. **TIER 1: Market Leaders** (established, broad coverage)
2. **TIER 2: Regional Champions** (strong local presence)
3. **TIER 3: Emerging/Innovative** (specialist, sustainable)

Prioritize suppliers with:
- Proven hospitality experience
- Strong ESG credentials (SBTi, ISO 14001, EcoVadis Gold/Platinum)
- Presence in ${region}
- Competitive pricing

Be specific and current (2026 market).`;

            const result = await callPerplexityAPI(prompt);
            
            loadingDiv.classList.remove('active');
            resultDiv.innerHTML = `<div class="result">${result}</div>`;
        }

        async function generateIntelligence() {
            const focus = document.getElementById('intel-focus').value;
            const geography = document.getElementById('intel-geography').value;
            const timeframe = document.getElementById('intel-timeframe').value;

            const loadingDiv = document.getElementById('intel-loading');
            const resultDiv = document.getElementById('intel-result');

            loadingDiv.classList.add('active');
            resultDiv.innerHTML = '';

            const prompt = `You are a market intelligence analyst for Accor's Astore procurement division. 

**Focus Area:** ${focus}
**Region:** ${geography}
**Timeframe:** ${timeframe}

Provide 4-5 hospitality-relevant intelligence items covering recent developments, trends, and procurement implications.

For each intelligence item, provide:

**HEADLINE:** Clear, specific title

**WHAT HAPPENED:** Brief summary (2-3 sentences) of the development, trend, or news

**WHY IT MATTERS FOR PROCUREMENT:** Direct implications for Astore category managers
- Cost impact (increase/decrease)
- Supply chain implications
- ESG/sustainability relevance
- Risk considerations
- Opportunity identification

**RECOMMENDED ACTION:** Specific next step (e.g., "Engage suppliers on X", "Monitor Y closely", "Prepare contingency for Z")

**SOURCE:** Cite source and date

Focus on:
- Market trends affecting hospitality services
- Supplier developments (M&A, innovations, challenges)
- Regulatory changes (especially ESG-related)
- Price movements and cost drivers
- Technology and innovation
- Labor market dynamics

Prioritize actionable, procurement-relevant insights. Be specific and current (${timeframe}).`;

            const result = await callPerplexityAPI(prompt);
            
            loadingDiv.classList.remove('active');
            resultDiv.innerHTML = `<div class="result">
                <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
                    <span class="insight-badge badge-esg">Strategic</span>
                    <span class="insight-badge badge-cost">Actionable</span>
                </div>
                ${result}
            </div>`;
        }

        async function generateTender() {
            const category = document.getElementById('tender-category').value;
            const region = document.getElementById('tender-region').value;
            const type = document.getElementById('tender-type').value;
            const context = document.getElementById('tender-context').value;

            const loadingDiv = document.getElementById('tender-loading');
            const resultDiv = document.getElementById('tender-result');

            loadingDiv.classList.add('active');
            resultDiv.innerHTML = '';

            const prompt = `Create a professional ${type} template for Accor Astore procurement:

**Category:** ${category}
**Region:** ${region}
**Requirements:** ${context}

Generate a complete, ready-to-use document with:

**1. INTRODUCTION & BACKGROUND**
- About Accor and Astore
- Scope of services required
- Contract value and duration
- Number of properties/locations

**2. TECHNICAL REQUIREMENTS**
- Service specifications for ${category}
- Quality standards and SLAs
- Technology/system requirements
- Reporting requirements

**3. ESG & SUSTAINABILITY REQUIREMENTS** (CRITICAL for 2026)
- Mandatory certifications (ISO 14001, etc.)
- Carbon reporting requirements (Scope 1, 2, 3)
- Social compliance (living wage, modern slavery)
- Circular economy commitments (where relevant)
- Diversity and inclusion metrics
- CSRD-aligned data requirements

**4. EVALUATION CRITERIA & WEIGHTINGS**
Provide specific scoring matrix:
- Technical capability (X%)
- ESG performance (X%)
- Price competitiveness (X%)
- Experience & references (X%)
- Innovation & value-add (X%)

For each criterion, define:
- What will be evaluated
- Scoring scale (e.g., 1-5 points)
- Minimum threshold

**5. SUPPLIER INFORMATION REQUIRED**
- Company profile
- Financial statements
- Client references
- Certifications
- ESG documentation

**6. SUBMISSION REQUIREMENTS**
- Format and structure
- Deadline
- Contact information

**7. KEY QUESTIONS TO ASK SUPPLIERS**
- 10-15 specific questions for ${category}
- Include both technical and ESG questions

Make it practical, professional, and hospitality-specific. Use clear language suitable for suppliers.`;

            const result = await callPerplexityAPI(prompt);
            
            loadingDiv.classList.remove('active');
            resultDiv.innerHTML = `<div class="result">
                <div class="info-box">
                    <strong>📋 Tender Document Generated</strong>
                    Copy this template and customize it further in your preferred format (Word, PDF).
                </div>
                ${result}
            </div>`;
        }
    </script>
</body>
</html>
