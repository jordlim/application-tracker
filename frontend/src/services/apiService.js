import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

// Fetch all applications
export const getApplications = async () => {
  try {
    const response = await axios.get(`${API_URL}applications/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching applications:', error);
    throw error;
  }
};

// Add other API methods as needed