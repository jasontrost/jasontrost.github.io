# Blog Management Guide

## How to Add a New Blog Post

### 1. Create Your New Post

Copy the template file (`liquidity-is-everything.html`) to create your new post:
```bash
cp liquidity-is-everything.html your-new-post-title.html
```

### 2. Edit Your Post

Update these key elements in your new file:

- **Title tags**: Update `<title>` and `<h1 class="post-title">`
- **Meta description**: Update the description meta tag
- **Date**: Update the post date in `<div class="post-meta">`
- **Content**: Replace the content in `<div class="post-content">`
- **Navigation**: Update the "Next" link in the footer

### 3. Add to Blog Index

Edit `index.html` and add your new post at the top of the posts list:

```html
<article class="blog-post">
    <h2 class="blog-post-title">
        <a href="/blog/your-new-post.html">Your Post Title</a>
    </h2>
    <div class="blog-post-meta">November 15, 2024 · 5 min read</div>
    <div class="blog-post-excerpt">
        <p>Your post excerpt goes here...</p>
        <a href="/blog/your-new-post.html" class="read-more">Read more →</a>
    </div>
</article>
```

### 4. Update Homepage Recent Posts (Optional)

If you want to feature your new post on the homepage, edit `/index.html` and update the "Recent Writing" section.

### 5. Update RSS Feed

Edit `rss.xml` and add your new post as the first `<item>` in the channel:

```xml
<item>
    <title>Your Post Title</title>
    <description>Your post description...</description>
    <link>https://jasontrost.github.io/blog/your-new-post.html</link>
    <guid isPermaLink="true">https://jasontrost.github.io/blog/your-new-post.html</guid>
    <pubDate>Fri, 15 Nov 2024 12:00:00 GMT</pubDate>
    <author>jason@smarkets.com (Jason Trost)</author>
    <content:encoded><![CDATA[
        Your post excerpt in HTML...
    ]]></content:encoded>
</item>
```

### 6. Commit and Push

```bash
git add .
git commit -m "Add new blog post: Your Post Title"
git push
```

## Writing Tips for Fintech Thought Leadership

### Structure
- **Strong opening**: Lead with your key insight or controversial take
- **Personal experience**: Use your 18 years of experience as proof
- **Data/Examples**: Include specific numbers, cases, or stories
- **Actionable insights**: End with what readers should do differently
- **Call to action**: Link to next post or invite discussion

### Tone
- **Confident**: You've been doing this for 18 years
- **Direct**: No hedging or excessive qualification
- **Contrarian**: Challenge conventional wisdom when you can back it up
- **Educational**: Teach what you've learned the hard way

### Topics That Position You as a Leader
- Market design and microstructure
- Regulatory navigation and compliance
- Liquidity dynamics and market making
- Fintech infrastructure and scaling
- Prediction market cycles and patterns
- Building in regulated industries
- Competing with incumbents

## Technical Notes

### URL Structure
Keep URLs simple and SEO-friendly:
- Good: `/blog/liquidity-is-everything.html`
- Bad: `/blog/2024-11-14-my-thoughts-on-liquidity-in-markets.html`

### Images
Place images in the `/blog/images/` directory (create if needed):
```html
<img src="/blog/images/your-image.jpg" alt="Description" loading="lazy">
```

### Code Examples
Use `<pre>` and `<code>` tags for code blocks:
```html
<pre><code>
// Your code here
</code></pre>
```

### Quotes
Use blockquotes for important callouts:
```html
<blockquote>
    <p>"Your memorable quote here."</p>
</blockquote>
```

## Maintenance

### When to Update
- Add new posts at least monthly
- Update RSS feed with each new post
- Rotate homepage featured posts every 2-3 posts
- Archive older posts (move down in index) after 10+ posts

### SEO Checklist
- [ ] Unique, descriptive title (50-60 chars)
- [ ] Meta description (150-160 chars)
- [ ] Open Graph tags for social sharing
- [ ] Meaningful URL slug
- [ ] Internal links to other posts
- [ ] External links to Smarkets where relevant

## Future Enhancements

Consider these upgrades as your blog grows:

1. **Static Site Generator**: Migrate to 11ty or Hugo for easier management
2. **Newsletter**: Add email subscription for new posts
3. **Comments**: Add Disqus or similar for engagement
4. **Analytics**: Track which posts resonate most
5. **Categories/Tags**: Organize posts by topic
6. **Search**: Add search functionality for 20+ posts

---

*Remember: The goal is establishing thought leadership in fintech. Every post should reinforce your expertise and unique perspective from 18 years in prediction markets.*