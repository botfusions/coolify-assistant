# N8N Webhook File Upload Interface

🚀 Modern, responsive web interface for uploading files to N8N webhooks with drag & drop support.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-green.svg)
![Coolify](https://img.shields.io/badge/coolify-compatible-purple.svg)

## ✨ Features

- 📤 **Drag & Drop**: Intuitive file upload experience
- 📁 **Multi-file Support**: Upload multiple files simultaneously  
- 📝 **Form Fields**: Name, email, and message inputs
- 📊 **Progress Tracking**: Real-time upload progress
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- 🔒 **Secure**: Client-side file validation and error handling
- 🐳 **Docker Ready**: Containerized with Nginx for optimal performance
- ☁️ **Coolify Compatible**: One-click deployment to any server

## 🎯 Use Cases

- **Document Submission**: Forms, applications, reports
- **Media Upload**: Images, videos, audio files
- **File Processing**: Automated workflows via N8N
- **Data Collection**: Survey responses with attachments
- **Content Management**: Blog posts, portfolio items

## 🚀 Quick Start

### Deploy with Coolify

1. **Create New Project** in Coolify Dashboard
2. **Add Resource** → **Application** → **Public Repository**
3. **Repository URL**: `https://github.com/botfusions/coolify-assistant.git`
4. **Build Pack**: Docker Compose
5. **Deploy** 🎉

### Local Development

```bash
# Clone repository
git clone https://github.com/botfusions/coolify-assistant.git
cd coolify-assistant

# Run with Docker
docker-compose up -d

# Access at http://localhost
```

## 🔧 Configuration

### Environment Variables

```env
# Domain configuration
COOLIFY_FQDN=your-domain.com

# Nginx settings
NGINX_HOST=localhost
NGINX_PORT=80

# N8N Webhook (configured in index.html)
N8N_WEBHOOK_URL=https://n8n.botfusions.com/webhook/11ef0598-b59d-4335-b797-a4b5a0402fa8
```

### Custom Domain

1. Set `COOLIFY_FQDN` environment variable
2. Configure DNS A record: `your-domain.com → your-server-ip`
3. SSL certificate will be auto-generated

## 📋 N8N Webhook Integration

### Data Format Sent to N8N

```javascript
FormData {
  // Form fields
  name: "User Name",
  email: "user@example.com", 
  message: "Optional message",
  timestamp: "2025-07-31T12:00:00.000Z",
  
  // Files (indexed)
  file_0: File,
  file_1: File,
  file_2: File,
  // ... more files
}
```

### N8N Workflow Setup

1. **Webhook Node**: Receive the POST request
2. **Extract Data**: Access form fields and files
3. **Process Files**: Save to storage, analyze, etc.
4. **Response**: Send success/error response

### CORS Configuration

If you encounter CORS errors, add these headers in your N8N HTTP Response node:

```json
{
  "headers": {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type"
  }
}
```

## 🎨 Customization

### Styling

The interface uses **Tailwind CSS**. Modify classes in `index.html`:

```html
<!-- Change color scheme -->
<div class="bg-indigo-600 hover:bg-indigo-700">
  <!-- Change to blue -->
  <div class="bg-blue-600 hover:bg-blue-700">
```

### File Validation

Add custom validation in the JavaScript:

```javascript
// File size limit (10MB example)
if (file.size > 10 * 1024 * 1024) {
  alert('File too large!');
  return;
}

// File type restriction
const allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
if (!allowedTypes.includes(file.type)) {
  alert('File type not allowed!');
  return;
}
```

### Form Fields

Add/remove form fields by modifying the HTML:

```html
<!-- Add new field -->
<div>
  <label class="block text-sm font-medium text-gray-700 mb-2">
    <i class="fas fa-phone mr-2"></i>Phone
  </label>
  <input type="tel" x-model="formData.phone" 
         class="w-full px-4 py-2 border border-gray-300 rounded-lg">
</div>
```

## 📁 File Structure

```
coolify-assistant/
├── index.html              # Main interface
├── Dockerfile              # Docker build configuration
├── nginx.conf              # Nginx server configuration
├── docker-compose.yml      # Container orchestration
├── README.md               # This file
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Actions (optional)
```

## 🐳 Docker Details

### Build Process

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

### Performance Features

- **Gzip Compression**: Enabled for all text assets
- **Caching Headers**: Static assets cached for 1 year
- **Security Headers**: XSS protection, CSRF prevention
- **Health Checks**: Container health monitoring

## 🔒 Security

### Client-Side Validation

- File size limits
- File type restrictions  
- Form field validation
- XSS prevention

### Server-Side Security

- Security headers via Nginx
- No executable uploads
- Request size limits
- HTTPS enforcement (with domain)

## 🐛 Troubleshooting

### Common Issues

**Build Fails**
```bash
# Check Docker logs
docker logs container-name

# Rebuild without cache  
docker-compose build --no-cache
```

**CORS Errors**
- Check N8N webhook CORS headers
- Verify webhook URL is correct
- Test webhook independently

**Upload Fails**
- Check N8N webhook timeout settings
- Verify file size limits in Nginx
- Check browser developer tools

**Mobile Issues**
- Test on real devices
- Check viewport meta tag
- Verify touch interactions

### Debug Mode

Enable console logging:

```javascript
// Add to index.html <script>
console.log('Files selected:', files);
console.log('Form data:', formData);
console.log('Upload response:', response);
```

## 📞 Support

- **Documentation**: [Coolify Docs](https://coolify.io/docs)
- **N8N Help**: [N8N Documentation](https://docs.n8n.io)
- **Issues**: [GitHub Issues](https://github.com/botfusions/coolify-assistant/issues)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Coolify](https://coolify.io) - Deployment platform
- [N8N](https://n8n.io) - Workflow automation
- [Tailwind CSS](https://tailwindcss.com) - Styling framework
- [Alpine.js](https://alpinejs.dev) - JavaScript framework
- [Font Awesome](https://fontawesome.com) - Icons

---

**Made with ❤️ by BotFusions**

Deploy your own instance: [![Deploy](https://img.shields.io/badge/Deploy-Coolify-purple.svg)](https://coolify.io)
