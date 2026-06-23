# Sea Level Prediction Platform - Complete Setup Guide

This is a full-stack application for predicting sea levels using machine learning. It includes a Next.js frontend, Flask backend, and Supabase database.

## Project Structure

```
├── app/                          # Next.js App Router pages
│   ├── page.tsx                 # Home page (landing)
│   ├── dashboard/page.tsx       # User dashboard with predictions
│   ├── analytics/page.tsx       # Analytics and charts
│   ├── settings/page.tsx        # User settings
│   └── auth/                    # Authentication pages
├── components/                   # Reusable React components
│   ├── prediction-form.tsx      # Prediction input form
│   ├── prediction-result.tsx    # Result display
│   └── analytics-charts.tsx     # Chart components
├── lib/
│   ├── supabase/               # Supabase client setup
│   └── api.ts                  # API utility functions
├── backend/                     # Flask Python backend
│   ├── app.py                  # Main Flask app
│   ├── requirements.txt        # Python dependencies
│   └── README.md               # Backend setup
└── Procfile                    # Deployment configuration
```

## Prerequisites

- Node.js 18+ and pnpm (or npm/yarn)
- Python 3.10+ (for local backend development)
- A Supabase account (https://supabase.com)
- Your ML model files (model.h5, scaler.pkl)

## Frontend Setup (Next.js)

### 1. Install Dependencies

```bash
pnpm install
```

### 2. Configure Environment Variables

Create a `.env.local` file:

```env
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
NEXT_PUBLIC_FLASK_API_URL=http://localhost:5000
```

### 3. Run Locally

```bash
pnpm dev
```

Open http://localhost:3000 in your browser.

## Backend Setup (Flask)

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Prepare Model Files

Create a `models/` directory and add your files:

```bash
cd backend
mkdir models
# Copy your model.h5 and scaler.pkl files here
```

### 3. Run Locally

```bash
python app.py
```

The API will be available at http://localhost:5000

### 4. Test the API

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 22.5,
    "pressure": 1013.25,
    "humidity": 65,
    "wind_speed": 12.5
  }'
```

## Database Setup (Supabase)

The database schema is automatically created via SQL migrations. Tables include:
- `profiles` - User profile information
- `predictions` - Store prediction results
- `prediction_history` - Track prediction history
- `datasets` - Store uploaded datasets
- `insights` - Store analysis insights

### Row-Level Security (RLS)

All tables have RLS policies enabled to ensure users only see their own data.

## Deployment Guide

### Option 1: Vercel (Frontend) + Render (Backend)

#### Frontend on Vercel

1. Push your code to GitHub
2. Go to https://vercel.com and connect your repository
3. Add environment variables:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - `NEXT_PUBLIC_FLASK_API_URL=https://your-backend.onrender.com`
4. Deploy

#### Backend on Render

1. Create a new Web Service on https://render.com
2. Connect your GitHub repository
3. Configure:
   - **Build Command:** `pip install -r backend/requirements.txt`
   - **Start Command:** `gunicorn app:app --chdir backend`
   - **Environment Variables:**
     - `MODEL_PATH=./backend/models/model.h5`
     - `SCALER_PATH=./backend/models/scaler.pkl`
   - **Disk:** Add persistent disk for model files
4. Deploy

### Option 2: Railway (Both Frontend & Backend)

Railway can deploy both apps in one project:

1. Create a new Railway project
2. Connect GitHub repository
3. Add `Procfile` for the backend
4. Configure environment variables
5. Deploy

### Uploading Model Files to Cloud

For cloud deployments, you need to store your model files:

#### Using AWS S3:
1. Create an S3 bucket
2. Upload model files
3. Configure IAM credentials
4. Update Flask app to download from S3

#### Using Render Disks:
1. Create a persistent disk in Render
2. Upload files to the disk
3. Mount the disk to your service

## Feature Walkthrough

### 1. Authentication
- Sign up with email and password
- Email verification required
- Secure session management with Supabase

### 2. Dashboard
- Input environmental parameters
- Get sea level predictions
- View confidence scores
- Store prediction history

### 3. Analytics
- Historical sea level trends
- Prediction accuracy comparison
- Key metrics dashboard
- Export data as CSV/PDF

### 4. Settings
- Update profile information
- Manage preferences
- Control data sharing options

## API Endpoints

### Prediction
```
POST /predict
{
  "temperature": float,
  "pressure": float,
  "humidity": float,
  "wind_speed": float
}
```

### Historical Data
```
GET /historical?limit=30&offset=0
```

### Insights
```
GET /insights/{dataset_id}
```

### Health Check
```
GET /health
```

## Common Issues & Solutions

### Issue: Model not loading
- Ensure model files are in the correct path
- Check file permissions
- Verify TensorFlow is installed: `pip install tensorflow`

### Issue: CORS errors
- Ensure `NEXT_PUBLIC_FLASK_API_URL` matches your backend URL
- Backend has CORS enabled for all origins

### Issue: Supabase connection failed
- Verify Supabase credentials
- Check network connectivity
- Ensure RLS policies allow your operations

### Issue: Authentication loop
- Clear browser cache/cookies
- Verify redirect URL is correct
- Check Supabase auth settings

## Performance Optimization

1. **Frontend:**
   - Enable Vercel Analytics
   - Use image optimization
   - Implement code splitting

2. **Backend:**
   - Cache model in memory
   - Use connection pooling
   - Consider async workers (Gunicorn workers > 1)

3. **Database:**
   - Add indexes on frequently queried columns
   - Monitor query performance
   - Archive old predictions regularly

## Security Considerations

1. **Environment Variables:**
   - Never commit `.env.local`
   - Use Vercel/Railway secrets manager
   - Rotate keys regularly

2. **Database:**
   - RLS policies enforce data isolation
   - Sensitive data encrypted at rest
   - Regular backups enabled

3. **API:**
   - Rate limiting recommended
   - Input validation on all endpoints
   - HTTPS only in production

## Monitoring & Maintenance

1. **Logging:**
   - Set up Vercel Analytics
   - Use Render logs for backend
   - Enable Supabase logs

2. **Uptime:**
   - Configure uptime monitors
   - Set up alerts for failures
   - Regular health checks

3. **Updates:**
   - Keep dependencies updated
   - Monitor security advisories
   - Test updates in staging

## Support & Resources

- Next.js Docs: https://nextjs.org/docs
- Flask Docs: https://flask.palletsprojects.com
- Supabase Docs: https://supabase.com/docs
- Render Docs: https://render.com/docs
- Vercel Docs: https://vercel.com/docs
