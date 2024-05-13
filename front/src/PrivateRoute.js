import { Navigate } from "react-router-dom";
import AuthService from "./services/Auth.service";

const PrivateRoute = ({ Component }) => {
 
  console.log(AuthService.isAuthenticated);
  return AuthService.isAuthenticated ? <Component /> : <Navigate to="/login" />;

};
export default PrivateRoute;