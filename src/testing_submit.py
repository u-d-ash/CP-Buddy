from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://codeforces.com/enter?back=/")
    page.fill('[name="handleOrEmail"]', "---")
    page.fill('[name="password"]', "---")
    page.click('[type="submit"]')

    # Wait for the login to complete
    page.wait_for_url("https://codeforces.com/")

    page.goto("https://codeforces.com/contest/1902/submit")

    page.locator('[name = "submittedProblemIndex"]').select_option(index=3)

    