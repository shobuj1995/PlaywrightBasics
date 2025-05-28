from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    try:
        BASE_URL = "https://opensource-demo.orangehrmlive.com"

        def goto_path(p, path):
            p.goto(f"{BASE_URL}{path}")

        # Use path only
        goto_path(page, "/web/index.php/auth/login")

    finally:
        # Save the trace even if error happens
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()


# Top-level code that provides the playwright instance
with sync_playwright() as playwright:
    run(playwright)
