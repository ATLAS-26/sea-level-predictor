# Sea Level Prediction Platform

A full-stack machine learning application for predicting sea level changes using advanced ML models, built with Next.js, Flask, and Supabase.

## Features

- **User Authentication**: Secure email-based authentication with Supabase
- **Prediction Engine**: Real-time sea level predictions using ML models
- **Analytics Dashboard**: Interactive charts and trend analysis
- **Data Management**: Upload and analyze CSV datasets
- **User Settings**: Profile management and preferences
- **Responsive Design**: Mobile-friendly interface with Tailwind CSS

## Tech Stack

### Frontend
- **Next.js 16** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first CSS framework
- **Shadcn/ui** - High-quality component library
- **Recharts** - Interactive charting library
- **Supabase SSR** - Authenticated client library

### Backend
- **Flask** - Python web framework
- **TensorFlow/Keras** - ML model framework
- **Scikit-learn** - Feature scaling and preprocessing
- **NumPy** - Numerical computations

### Database
- **Supabase PostgreSQL** - Managed database with auth
- **Row-Level Security** - Data isolation per user

## Quick Start

### Prerequisites
- Node.js 18+
- Python 3.10+
- Supabase account

### 1. Clone & Install

```bash
# Frontend dependencies
pnpm install

# Backend dependencies
cd backend
pip install -r requirements.txt
```

### 2. Environment Setup

Create `.env.local`:
```env
NEXT_PUBLIC_SUPABASE_URL=your_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_key
NEXT_PUBLIC_FLASK_API_URL=http://localhost:5000
```

### 3. Run Locally

```bash
# Terminal 1 - Frontend
pnpm dev

# Terminal 2 - Backend
cd backend
python app.py
```

Visit http://localhost:3000

## Project Structure

```
├── app/                    # Next.js pages
│   ├── page.tsx           # Landing page
│   ├── dashboard/         # Prediction interface
│   ├── analytics/         # Charts & insights
│   ├── settings/          # User profile
│   └── auth/              # Authentication
├── components/            # Reusable React components
│   ├── prediction-form.tsx
│   ├── prediction-result.tsx
│   ├── analytics-charts.tsx
│   └── csv-upload.tsx
├── lib/
│   ├── supabase/          # Client setup
│   └── api.ts             # API utilities
├── backend/               # Flask server
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
└── SETUP.md              # Detailed setup guide
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/predict` | POST | Make a prediction |
| `/historical` | GET | Get historical data |
| `/insights/{id}` | GET | Get dataset insights |
| `/health` | GET | Health check |

## Deployment

### Frontend (Vercel)
```bash
# Push to GitHub, then:
# 1. Connect repo to Vercel
# 2. Add environment variables
# 3. Deploy
```

### Backend (Render)
```bash
# 1. Create Web Service on Render
# 2. Connect GitHub repo
# 3. Set start command: gunicorn app:app --chdir backend
# 4. Add persistent disk for models
# 5. Deploy
```

See [SETUP.md](./SETUP.md) for detailed deployment guide.

## Usage

### 1. Sign Up
Create an account with email and password.

### 2. Make a Prediction
Go to Dashboard, enter environmental parameters:
- Temperature (°C)
- Pressure (hPa)
- Humidity (%)
- Wind Speed (m/s)

### 3. View Analytics
Check historical trends and prediction accuracy in the Analytics section.

### 4. Upload Datasets
Upload CSV files to analyze multiple data points.

### 5. Manage Profile
Update settings and preferences in Settings.

## Database Schema

### Profiles
- User profile information
- RLS: Users can only access their own

### Predictions
- Prediction results
- Input parameters
- Timestamps

### Datasets
- Uploaded CSV files
- Metadata

### Insights
- Analysis and metrics
- Historical trends

### Prediction History
- Track all predictions
- Audit log

## Development

### Add Dependencies

Frontend:
```bash
pnpm add package-name
```

Backend:
```bash
cd backend
pip install package-name
pip freeze > requirements.txt
```

### Run Tests
```bash
# Frontend
pnpm test

# Backend
cd backend
pytest
```

### Build for Production
```bash
# Frontend
pnpm build

# Backend
gunicorn app:app --chdir backend
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Supabase connection error | Check env variables are set correctly |
| Model not loading | Verify model files exist at specified paths |
| CORS errors | Ensure backend URL matches in env |
| Build fails | Run `pnpm install && pnpm build` |

## Security

- RLS policies on all database tables
- Secure password hashing
- HTTP-only session cookies
- Environment variables not committed
- CORS configured for known origins

## Performance

- Server-side rendering (SSR) for auth pages
- Static generation for public pages
- Image optimization
- Database query optimization
- Model caching

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Run tests
5. Submit pull request

## License

MIT License - See LICENSE file for details

## Support

- Docs: See SETUP.md
- Issues: GitHub Issues
- Email: support@example.com

## Resources

- [Next.js Docs](https://nextjs.org/docs)
- [Flask Docs](https://flask.palletsprojects.com)
- [Supabase Docs](https://supabase.com/docs)
- [Tailwind CSS](https://tailwindcss.com)
