import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Retail Product Attribute Quality',
  description: 'Multi-agent product data quality and attribute classification dashboard',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
