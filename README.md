# minimal-bootstrap-blog

## Introduction

![minimal-bootstrap-blog dark mode homepage](https://user-images.githubusercontent.com/13270895/126380100-f61f3464-1604-486c-89ac-5a7b98fe3ce7.png)
![minimal-bootstrap-blog light mode homepage](https://user-images.githubusercontent.com/13270895/126380111-35619141-0e9d-4780-a2c9-1c8992497f56.png)
![minimal-bootstrap-blog mobile homepages](https://user-images.githubusercontent.com/13270895/126383023-8fa01fd7-544b-459d-956e-4a67a735758b.png)

minimal-bootstrap-blog is a no frills, fully-responsive, hyper-minimalistic dark/light theme made with bootstrap-dark-5: https://github.com/vinorodrigues/bootstrap-dark-5. The theme is heavily inspired by Mark Otto's personal site: https://markdotto.com/

#### Features

- Automatically changes from dark/light modes depending on the OS settings.
- Easy integration with Google Analytics.
- Generates XML sitemap and RSS Atom feed.
- jekyll-seo-tag to add metadata tags for search engines and social networks to better index and display your site's content.

## Installation

Clone this repo:

    $ git clone https://github.com/andrewhwanpark/minimal-bootstrap-blog.git

If you haven't already, install bundler:

    $ gem install bundler

And then execute:

    $ bundle install

Serve the site:

    $ bundle exec jekyll serve

# Installation with Github Pages

After cloning the repo, checkout to the gh-pages branch.

    $ git checkout gh-pages && git pull

In the directory:

    $ bundle install

For local development:

    $ bundle exec jekyll serve

Now, you can publish the site. Under your repository name, click Settings.

![tutorial](https://docs.github.com/assets/images/help/repository/repo-actions-settings.png)

In the left sidebar, click Pages.

![tutorial 2](https://docs.github.com/assets/images/help/pages/pages-tab.png)

To see your published site, under "GitHub Pages", click your site's URL.

![tutorial 3](https://docs.github.com/assets/images/help/pages/click-pages-url-to-preview.png)

For a more detailed guide, visit this guide by Github: https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll

## Usage

### First things first: \_config.yml

First, you should change data in \_config.yml to the appropriate information such as your social links for the footer icons.

### Adding content

In order to add permanent pages, add in similar fashion to about.md and portfolio.md and add apppropriate data to \_data/navigation.yml.

In order to add blog posts, add in similar fashion to \_posts/2021-07-16-this-post-demonstrates-post-content-styles.md.

### Custom style changes

If you wish to add custom styling through SCSS or CSS, you can add or edit \_sass/main.scss.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/andrewhwanpark/minimal-bootstrap-blog.

## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
