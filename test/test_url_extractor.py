import unittest

from worker.url_extractor import extract_detail_urls
from worker.url_extractor import extract_url_13f_xml


class URLExtractorTest(unittest.TestCase):
    def test_extract_detail_urls_whenGivenCorrectURL(self):
        correct_url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001067983&type=13F%25&start=0&count=100'
        actual_urls = extract_detail_urls(correct_url)

        expected1 = 'https://www.sec.gov/Archives/edgar/data/1067983/000095012316022377/0000950123-16-022377-index.htm'
        self.assertTrue(expected1 in actual_urls)

        expected2 = 'https://www.sec.gov/Archives/edgar/data/1067983/000095015004000233/0000950150-04-000233-index.htm'
        self.assertTrue(expected2 in actual_urls)

        self.assertEquals(100, len(actual_urls))

    def test_extract_detail_urls_whenGivenIncorrectURL(self):
        incorrect_url = 'https://www.sec.gov/'
        urls = extract_detail_urls(incorrect_url)
        self.assertEquals(0, len(urls))

    def test_extract_detail_urls_whenGivenNoneURL(self):
        none_url = 'NoneURL'
        urls = extract_detail_urls(none_url)
        self.assertEquals(0, len(urls))

    def test_extract_url_13f_xml_whenGivenURLWithXML(self):
        url = 'https://www.sec.gov/Archives/edgar/data/1067983/000095012316022377/0000950123-16-022377-index.htm'
        actual_urls = extract_url_13f_xml(url)

        expected_urls = ['https://www.sec.gov/Archives/edgar/data/1067983/000095012316022377/form13fInfoTable.xml']

        self.assertEquals(expected_urls, actual_urls)

    def test_extract_url_13f_xml_whenGivenURLWithoutXML(self):
        url = 'https://www.sec.gov/Archives/edgar/data/1067983/000095015004000233/0000950150-04-000233-index.htm'
        actual_urls = extract_url_13f_xml(url)

        expected_urls = []

        self.assertEquals(expected_urls, actual_urls)

    def test_extract_url_13f_xml_whenGivenNoneURL(self):
        none_url = 'NoneURL'
        urls = extract_url_13f_xml(none_url)
        self.assertEquals(0, len(urls))


if __name__ == '__main__':
    unittest.main()
