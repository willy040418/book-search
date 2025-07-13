import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'  # Nama spider harus 'books' sesuai instruksi
    allowed_domains = ['books.toscrape.com']  # Batasi domain
    start_urls = ['https://books.toscrape.com/']  # URL awal

    def parse(self, response):
        # Ekstrak data dari setiap buku di halaman
        for book in response.css('article.product_pod'):
            yield {
                'title': book.css('h3 a::attr(title)').get(),  # Judul lengkap
                'price': book.css('p.price_color::text').get(),  # Harga
                'rating': book.css('p.star-rating::attr(class)').get().split()[-1],  # Rating (e.g., 'Five')
                'url': response.urljoin(book.css('h3 a::attr(href)').get())  # URL buku lengkap
            }

        # Pagination: Ikuti link halaman selanjutnya jika ada
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
