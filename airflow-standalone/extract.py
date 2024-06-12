import pandas as pd
from apify_client import ApifyClient


def extract():
    # Initialize the ApifyClient with your API token
    client = ApifyClient("apify_api_Tt6z8VyODP22kqrlq6IFNHBixGEsNu40JTM1")

    # Prepare the Actor input
    run_input = {
        "startUrls": [{ "url": "https://crawlee.dev" }],
        "keepUrlFragments": False,
        "globs": [{ "glob": "https://crawlee.dev/*/*" }],
        "pseudoUrls": [],
        "excludes": [{ "glob": "/**/*.{png,jpg,jpeg,pdf}" }],
        "linkSelector": "a[href]",
        "pageFunction": """async function pageFunction(context) {
        const { $, request, log } = context;

        // The \"$\" property contains the Cheerio object which is useful
        // for querying DOM elements and extracting data from them.
        const pageTitle = $('title').first().text();

        // The \"request\" property contains various information about the web page loaded. 
        const url = request.url;
        
        // Use \"log\" object to print information to actor log.
        log.info('Page scraped', { url, pageTitle });

        // Return an object with the data extracted from the page.
        // It will be stored to the resulting dataset.
        return {
            url,
            pageTitle
        };
    }""",
        "proxyConfiguration": { "useApifyProxy": True },
        "proxyRotation": "RECOMMENDED",
        "initialCookies": [],
        "additionalMimeTypes": [],
        "forceResponseEncoding": False,
        "ignoreSslErrors": False,
        "preNavigationHooks": """// We need to return array of (possibly async) functions here.
    // The functions accept two arguments: the \"crawlingContext\" object
    // and \"requestAsBrowserOptions\" which are passed to the `requestAsBrowser()`
    // function the crawler calls to navigate..
    [
        async (crawlingContext, requestAsBrowserOptions) => {
            // ...
        }
    ]""",
        "postNavigationHooks": """// We need to return array of (possibly async) functions here.
    // The functions accept a single argument: the \"crawlingContext\" object.
    [
        async (crawlingContext) => {
            // ...
        },
    ]""",
        "maxRequestRetries": 3,
        "maxPagesPerCrawl": 0,
        "maxResultsPerCrawl": 0,
        "maxCrawlingDepth": 0,
        "maxConcurrency": 50,
        "pageLoadTimeoutSecs": 60,
        "pageFunctionTimeoutSecs": 60,
        "debugLog": False,
        "customData": {},
    }

    # Run the Actor and wait for it to finish
    run = client.actor("YrQuEkowkNCLdk4j2").call(run_input=run_input)

    final_df = pd.DataFrame()

    # Fetch and print Actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)
        temp_df = pd.DataFrame.from_dict([item])
        print(temp_df)
        temp_df.reset_index(inplace=True)
        print(temp_df)
        print(type(temp_df))
        print(type(final_df))
        final_df = pd.concat([final_df, temp_df], axis=0)

    print(final_df)

    # Add the above dataframe data to a csv
    final_df.to_csv("apify_crawlee_extract.csv")


    print("//////////////////////////////////////")
        