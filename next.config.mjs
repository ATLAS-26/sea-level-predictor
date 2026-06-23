/** @type {import('next').NextConfig} */
const nextConfig = {
  typescript: {
    ignoreBuildErrors: true,
  },
  images: {
    unoptimized: true,
  },
  experimental: {
    turbo: {
      ignoreFileSystemPublicRoutes: true,
    },
  },
  allowedDevOrigins: ['http://192.168.1.7'],
}

export default nextConfig
