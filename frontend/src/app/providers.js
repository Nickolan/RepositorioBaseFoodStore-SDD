import { jsx as _jsx } from "react/jsx-runtime";
import '@/app/index.css';
import { QueryClientProvider } from '@tanstack/react-query';
import { queryClient } from '@/shared/config';
export function Providers({ children }) {
    return (_jsx(QueryClientProvider, { client: queryClient, children: children }));
}
//# sourceMappingURL=providers.js.map