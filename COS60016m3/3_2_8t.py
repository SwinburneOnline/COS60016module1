
import requests
import gr
urls = {'google': 'https://www.google.com', 'httpbin': {'url': 'https://httpbin.org', 'uri': ('get', 'response-headers', 'post')}}

class PostRequest:
    @classmethod
    def make_post_request(self, url, data=None, headers=None):
        return requests.post(url=url, data=data, headers=headers)

pr = PostRequest()

headers_post = {'User-Agent': 'Godzilla'}
data = {'first_name': 'Ana', 'last_name': 'Storm', 'age': '24'}

resp = pr.make_post_request(url=urls['httpbin']['url'] + '/' + urls['httpbin']['uri'][2], data=data, headers=headers_post)

print(gr.print_response_headers(resp.headers))
print("STATUS_CODE: ", resp.status_code)
print(resp.text)
print(resp.url)
