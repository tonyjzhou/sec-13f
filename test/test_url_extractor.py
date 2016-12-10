import unittest

from worker.url_extractor import extract_detail_urls


class URLExtractorTest(unittest.TestCase):
    def test_extract_detail_urls(self):
        collection_url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001067983&type=13F%25&start=0&count=100'
        urls = extract_detail_urls(collection_url)
        self.assertTrue(
            'https://www.sec.gov/Archives/edgar/data/1067983/000095012316022377/0000950123-16-022377-index.htm' in urls)
        self.assertTrue(
            'https://www.sec.gov/Archives/edgar/data/1067983/000095015004000233/0000950150-04-000233-index.htm' in urls)
        self.assertEquals(100, len(urls))


if __name__ == '__main__':
    unittest.main()
